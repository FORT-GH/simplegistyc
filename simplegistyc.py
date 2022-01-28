import gistyc  #|
import os      #| - import modules

class api():

    def create_gist(filepath, text , token):
        file = open(filepath, "w+") #|
        file.write(text)            #| - creating a file named "filepath" and the text "text"
        file.close()                #|
        gist_api = gistyc.GISTyc(auth_token=token)              #|
        response_data = gist_api.create_gist(file_name=filepath)#| - Create a GIST
        os.remove(filepath) # remove file "filepath"
        return response_data

    def update_gist(filepath, text , token , id):
        file = open(filepath, "w+")#|
        file.write(text)           #| - creating a file named "filepath" and the text "text"
        file.close()               #|
        gist_api = gistyc.GISTyc(auth_token=token)                                 #|
        response_update_data = gist_api.update_gist(file_name=filepath, gist_id=id)#| - Update a GIST
        os.remove(filepath) # remove file "filepath"
        return response_update_data

    def update_urlgists(filepath , token):
        gist_api = gistyc.GISTyc(auth_token = token)                                     #|
        response_text = str(gist_api.get_gists()).split("'")                             #| - Get new url raw a GIST
        response_text_url = response_text[response_text.index(filepath) + 16]            #|
        return response_text_url

"""
TOKEN: is the GIST access token
FILEPATH: the name of the imaginary file (with extension)
TEXT: text in FILEPATH
ID_GIST: ID of a GIST

Example:
    create = simplegistyc.api.create_gist(filepath = FILEPATH , text = TEXT , token = TOKEN)
    update = simplegistyc.api.update_gist(filepath = FILEPATH , text = TEXT , token = TOKEN , id = ID_GIST)
    update_url = simplegistyc.api.update_urlgists(filepath = FILEPATH , auth_token = TOKEN)
"""
