from flask import escape
import functions_framework
import json

@functions_framework.http
def hello_http(request):

    # pockets, this is will be a number 
    # boneloss, this is also be a number 
    # idea: we will sum pokets + boneloss, to get some count 
    # if the count is above 7+5=12, so if >7 , return response
    # but also say that they have periodontitis  

    request_args = request.args

    if request_args and "pockets" in request_args:
        pockets_depths = request_args["pockets"]
    else:
        pockets_depths = 7


    if request_args and "boneloss" in request_args:
        boneloss_value = request_args["boneloss"]
    else:
        boneloss_value = 5


    # Step 1 convert everything to numbers 
    pockets_num = int(pockets_depths)
    boneloss_num = int(boneloss_value)

    # Step 2 we now some them all together 
    perio_sum = pockets_num + boneloss_num 

    # Step 3 create a json object to return to the user 
    output = json.dumps(
        {
            "entered_pockets" : pockets_num, 
            "entered_boneloss": boneloss_num, 
            "perio_sum" : perio_sum
        }
    )

    return output



