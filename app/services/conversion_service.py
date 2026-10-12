"""
Conversion service.

Orchestrates a batch WEBP conversion job on a background thread and
computes the final statistics. The UI layer only reacts to signals.
"""

import time

from PySide6.QtCore import QObject, Signal

from app.core.conversion_thread import ConversionThread
from app.core.performance_config import PerformanceConfig


class ConversionService(QObject):
    """
    Runs one conversion job at a time and reports progress/results.

    Signals:
        progress_changed(progress, success, failed)
        file_processed(filename)
        worker_changed(active, maximum)
        state_changed(is_running)
        finished(result_dictionary)
        failed(error_message)
    """

    progress_changed = Signal(int, int, int)
    file_processed = Signal(str)
    worker_changed = Signal(int, int)
    state_changed = Signal(bool)
    finished = Signal(dict)
    failed = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.thread = None
        self.start_time = None

    # ------------------------------------------------------------------
    # STATE
    # ------------------------------------------------------------------

    def is_running(self) -> bool:
        return self.thread is not None

    def get_worker_count(self) -> int:
        """Recommended worker count for the current hardware."""
        try:
            config = PerformanceConfig()
            return config.calculate_workers()
        except Exception:
            return 0

    # ------------------------------------------------------------------
    # START / CANCEL
    # ------------------------------------------------------------------

    def start(self, images, settings, output_folder):
        """Begin a conversion job in the background."""
        if self.is_running():
            return False

        thread = ConversionThread(images, settings, output_folder)
        thread.worker_changed.connect(self.worker_changed)
        thread.file_processed.connect(self.file_processed)
        thread.progress_changed.connect(self.progress_changed)
        thread.conversion_finished.connect(self._on_finished)
        thread.conversion_failed.connect(self._on_failed)
        thread.finished.connect(self._cleanup_thread)

        self.thread = thread
        self.start_time = time.perf_counter()
        self.state_changed.emit(True)
        thread.start()
        return True

    def cancel(self):
        if self.thread:
            self.thread.cancel()

    # ------------------------------------------------------------------
    # THREAD HANDLERS
    # ------------------------------------------------------------------

    def _on_finished(self, result):
        result = {
            "success": result["success"],
            "failed": result["failed"],
            "cancelled": result.get("cancelled", False),
            "input_bytes": result["input_bytes"],
            "output_bytes": result["output_bytes"],
            "saved_percent": result["saved_percent"],
        }
        result.update(self._build_statistics(result))
        self.state_changed.emit(False)
        self.finished.emit(result)

    def _on_failed(self, error):
        self.state_changed.emit(False)
        self.failed.emit(error)

    def _cleanup_thread(self):
        thread = self.thread
        self.thread = None
        if thread:
            thread.deleteLater()
        self.state_changed.emit(False)

    # ------------------------------------------------------------------
    # STATISTICS
    # ------------------------------------------------------------------

    def _build_statistics(self, result) -> dict:
        duration = 0.0
        if self.start_time:
            duration = time.perf_counter() - self.start_time

        total = result["success"] + result["failed"]
        speed = total / duration if duration > 0 else 0

        return {
            "total": total,
            "duration": duration,
            "speed": speed,
            "input_mb": result["input_bytes"] / (1024 * 1024),
            "output_mb": result["output_bytes"] / (1024 * 1024),
        }