import os

if os.environ.get("DEBUG", False) == "true":
    import ptvsd

    print("waiting for debugger... you should start it now")
    # Enable ptvsd on 0.0.0.0 address and on port 5890 that we'll connect later with our IDE
    ptvsd.enable_attach(address=("0.0.0.0", 5858), redirect_output=True)
    ptvsd.wait_for_attach()
    print("debugger attached")
