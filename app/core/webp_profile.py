WEBP_PROFILES = {


    "fast": {

        "method": 2,

        "name": "Fast Conversion",

        "description":
            "Prioritize conversion speed"

    },


    "balanced": {

        "method": 4,

        "name": "Standard Quality",

        "description":
            "Balance between speed and compression"

    },


    "compression": {

        "method": 6,

        "name": "Maximum Compression",

        "description":
            "Smallest file size with slower conversion"

    }

}





DEFAULT_PROFILE = "fast"





def get_webp_method(profile=None):


    """
    Return WEBP encoder method.

    Method:
        2 = Fast
        4 = Balanced
        6 = Maximum Compression
    """



    if not isinstance(
            profile,
            str
    ):


        profile = DEFAULT_PROFILE



    if profile not in WEBP_PROFILES:


        profile = DEFAULT_PROFILE



    return WEBP_PROFILES[profile]["method"]





def get_profile_info(profile=None):


    """
    Return profile metadata.
    """


    if not isinstance(
            profile,
            str
    ):


        profile = DEFAULT_PROFILE



    return WEBP_PROFILES.get(

        profile,

        WEBP_PROFILES[DEFAULT_PROFILE]

    )





def get_available_profiles():


    """
    Used by UI.
    """


    return WEBP_PROFILES