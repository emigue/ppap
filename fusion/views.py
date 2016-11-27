from __future__ import absolute_import

import logging
from django.shortcuts import render
from fusion.forms import FusionForm
from fusion.models import Fusion, Apple, Pineapple, Membrillo, Pen

logger = logging.getLogger(__name__)


def index(request):
    """
    View to view PPAP main page and create fusion between fruit and pen.
    :param request: Request
    :return: HTTPResponse
    """

    if request.method == 'POST':
        form = FusionForm(request.POST)
        if form.is_valid():
            fruit = form.cleaned_data['fruit']
            has_pen = form.cleaned_data['has_pen']

            if has_pen:
                if fruit == '1':
                    fruit = Apple.objects.create()
                elif fruit == '2':
                    fruit = Pineapple.objects.create()
                elif fruit == '3':
                    fruit = Membrillo.objects.create()
                else:
                    err_msg = "Invalid fruit selected"
                    logger.error(err_msg)
                    raise ValueError(err_msg)

                pen = Pen.objects.create()
                fusion = Fusion.objects.create(left_hand=fruit, right_hand=pen)
                logger.info("Created fusion {0}".format(fusion))
            else:
                logger.error("Fusion not created. Missing pen.")
        else:
            logger.warn("Invalid fusion form")
    else:
        form = FusionForm()
    fusions = Fusion.objects.all()
    return render(request, 'fusion/main.html',
                  {'form': form,
                   'fusion_list': fusions})
