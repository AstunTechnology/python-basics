# OS Names API

**Note:** these exercises expect that you have registered for a user account and acquired an API key, and that 
you have saved that key in a `secrets.py` file in `dict` called `secrets` with at least a member `key` with 
the value of that API Key. That file must be in the working directory where the rest of your code is.

## Part 1 - Local Type

Taking the file [`get_names.py`](get_names.py) as a starting point add functionality to extend the programs 
behaviour to take a `LOCAL_TYPE` to restrict the results by passing in a `fq` parameter as described in the 
[technical specification](https://osdatahub.os.uk/docs/names/technicalSpecification). 

## Part 2 - Local Types

Now modify your program to handle more than one `LOCAL_TYPE` at a time. 

## Part 3 - Limit by Type

The results include a field `TYPE` but for some reason it isn't possible to limit API results by that value. 
See if you can extend your last program to allow a user to limit their request by `TYPE` such as 
`populatedPlace`. 


# Solutions

If you get completely stumped here are the [solutions](assets/names.zip) for you to try and decipher.
