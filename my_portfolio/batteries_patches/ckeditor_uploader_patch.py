from __future__ import absolute_import, unicode_literals

import os

from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.utils.html import escape
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from ckeditor_uploader import utils
from ckeditor_uploader.backends import registry
from ckeditor_uploader.utils import storage
from ckeditor_uploader.views import get_upload_filename


class ImageUploadView(generic.View):
    http_method_names = ["post"]

    def post(self, request, **kwargs):
        """
        Uploads a file and send back its URL to CKEditor.
        """
        uploaded_file = request.FILES["upload"]

        backend = registry.get_backend()

        ck_func_num = request.GET.get("CKEditorFuncNum")
        if ck_func_num:
            ck_func_num = escape(ck_func_num)

        filewrapper = backend(storage, uploaded_file)
        allow_nonimages = getattr(settings, "CKEDITOR_ALLOW_NONIMAGE_FILES", True)
        # Throws an error when an non-image file are uploaded.
        if not filewrapper.is_image and not allow_nonimages or len(uploaded_file.read()) > 1024 * 1024 * 5:
            return HttpResponse(
                """
                <script type='text/javascript'>
                window.parent.CKEDITOR.tools.callFunction({0}, '', 'Invalid file.');
                </script>""".format(
                    ck_func_num
                )
            )

        filepath = get_upload_filename(uploaded_file.name, request)

        saved_path = filewrapper.save_as(filepath)

        url = utils.get_media_url(saved_path)

        if ck_func_num:
            # Respond with Javascript sending ckeditor upload url.
            return HttpResponse(
                """
            <script type='text/javascript'>
                window.parent.CKEDITOR.tools.callFunction({0}, '{1}');
            </script>""".format(
                    ck_func_num, url
                )
            )
        else:
            _, filename = os.path.split(saved_path)
            retdata = {"url": url, "uploaded": "1", "fileName": filename}
            return JsonResponse(retdata)

upload = csrf_exempt(ImageUploadView.as_view())
