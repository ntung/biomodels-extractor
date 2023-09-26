import requests

from constants import API_URL


# GET /{model_id}?format=json|xml
def get_model_info(model_id, out_format="json"):
    response = requests.get(API_URL + "/" + model_id + "?format=" + out_format)
    if out_format == "xml":
        # todo: implement me
        output = None
    else:
        output = response.json()
    return output


# GET /model/files/{model_id}
def get_model_files_info(model_id, out_format="json"):
    response = requests.get(API_URL + "/model/files/" + model_id + "?format=" + out_format)
    if out_format == "xml":
        # todo: implement me
        output = None
    else:
        output = response.json()
    return output


# GET /model/identifiers
def get_model_identifiers(out_format="json"):
    response = requests.get(API_URL + "/model/identifiers?format=" + out_format)
    return response.json()


def main():
    all_ids = get_model_identifiers()
    model_ids = all_ids["models"]
    # [print(m) for m in model_ids]
    for m in model_ids:
        files_info = get_model_info(m)["files"]
        if "additional" in files_info:
            additional_files_info = files_info["additional"]
            is_sedml = False
            file_name_list = []
            for file in additional_files_info:
                file_name_list.append(file["name"])
                if file["name"].endswith(".sedml"):
                    is_sedml = True
                    break
            if is_sedml:
                print(m)


if __name__ == "__main__":
    main()
