from rest_framework.views import APIView
from cc_app.models import VideoUpload
from cc_app.serializers import OutputLocationSerializer
from cc_app.models import OutputLocationSetter
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework import status
import subprocess


# Create your views here.
# class CCExtractorView(View):
#     form_class = OutputLocationForm

#     def run_ccextractor(self, command):
#         cc_command = "ccextractor" +

#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():


class FileUploadView(APIView):
    parser_classes = [FileUploadParser]

    def post(self, request, filename, format="mp4"):
        file_obj = request.data.get("file")
        # serializer = VideoUploadSerializer(data=file_obj)
        video_upload = VideoUpload.objects.create(video_file=file_obj)
        output_subtitle_path = f"output/subs{video_upload.pk}.srt"

        destination_path = f"input/{filename}"
        video_path = destination_path

        ccextractor_command = f"ccextractor -o {output_subtitle_path} {video_path}"

        result = subprocess.run(ccextractor_command, shell=True)

        if result.returncode == 0:
            # The subtitle extraction was successful
            return Response(
                {"message": "File uploaded and subtitle extracted successfully"},
                status=status.HTTP_201_CREATED,
            )
        else:
            # An error occurred during subtitle extraction
            error_message = f"Error executing ccextractor command: {ccextractor_command}\nReturn Code: {result.returncode}"
            return Response(
                {"error": error_message},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        # else:
        #     return Response(serializer.errors)
