# -*- coding: utf-8 -*-

"""
***************************************************************************
    cdilate.py
    ---------------------
    Date                 : August 2012
    Copyright            : (C) 2012 by Victor Olaya
    Email                : volayaf at gmail dot com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

__author__ = 'Victor Olaya'
__date__ = 'August 2012'
__copyright__ = '(C) 2012, Victor Olaya'
# This will get replaced with a git SHA1 when you do a git archive
__revision__ = '$Format:%H$'

##Conditioning_image=raster
##iterations=number 1
from sextante.pymorph.mmorph import cdilate, binary
img2 = gdal.Open(Conditioning_image)
input_array2 = img2.ReadAsArray()
output_array = cdilate(binary(input_array), binary(input_array2), n=iterations)
