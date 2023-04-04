The warnings module is a built-in Python library that allows you to control the display of warning messages. To turn off warning messages, you can use the warnings.filterwarnings() function. For example, This will disable the display of all warning messages.

    import warnings
    warnings.filterwarnings('ignore')

If you want to enable the display of warning messages, you can use the 'default' or 'always' argument instead of 'ignore'. For example:

    import warnings 
    warnings.filterwarnings('default')

ref: [noteable.io/blog/disable-warnings-in-jupyter](https://noteable.io/blog/disable-warnings-in-jupyter/#:~:text=The%20warnings%20module%20is%20a,display%20of%20all%20warning%20messages.)
