from django.core.files.uploadedfile import InMemoryUploadedFile


class FileCnab:
    
    def __init__(self, request, file: InMemoryUploadedFile):
        if(request.method == "GET"):
            self.file = file
            self.operations = self.operations_infos()
            
        if(request.method == "POST"):
            self.file = file
            self.operations = self.operations_infos()


    def operations_infos(self, data):
        return data


