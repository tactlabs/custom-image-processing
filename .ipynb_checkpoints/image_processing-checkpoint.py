{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "d5cb5fdd-f9fb-4bca-ab58-9455beac376e",
   "metadata": {},
   "outputs": [],
   "source": [
    "from wand.image import Image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "51f361a7-8536-4789-b206-6680c8e07079",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1295 1500\n"
     ]
    }
   ],
   "source": [
    "oreo = Image(filename ='SL1500.jpg')\n",
    "print(oreo.height, oreo.width)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "c3811c61-2b1d-45cb-a834-3272644cb938",
   "metadata": {},
   "outputs": [],
   "source": [
    "oreo_convert = oreo.convert('png')\n",
    "oreo_convert.save(filename ='converted-oreo.png')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "c18a7dcd-aff4-4fe9-895f-57fdfa66abe7",
   "metadata": {},
   "outputs": [],
   "source": [
    "oreo.blur(sigma = 5)\n",
    "oreo.save(filename =\"oreo-blur.jpg\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "be71db2a-d96b-419f-9377-aaeaf7c307a5",
   "metadata": {},
   "outputs": [],
   "source": [
    "flip_oreo = oreo.clone()\n",
    "flip_oreo.flip()  \n",
    "flip_oreo.save(filename ='flip-oreo.jpg')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "e289ce48-dc50-45dc-ad28-9a1127db5d5d",
   "metadata": {},
   "outputs": [],
   "source": [
    "rotate_oreo = oreo.clone()\n",
    "rotate_oreo.rotate(45)  \n",
    "rotate_oreo.save(filename ='rotate-oreo.jpg')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "bd087996-0df1-4f00-bdb3-1617ea8b8f76",
   "metadata": {},
   "outputs": [],
   "source": [
    "oreo.crop(100, 100)\n",
    "oreo.save(filename = 'oreo-cropped.jpg')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "1ee5a0c8-7842-46f2-8803-c6d7189a628d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1000 1000\n"
     ]
    }
   ],
   "source": [
    "resize_oreo=oreo.resize(1000,1000)\n",
    "print(oreo.width, oreo.height)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "41790064-181c-436a-bff4-81f58692d392",
   "metadata": {},
   "source": [
    "ny = Image(filename ='pdf new york.pdf')\n",
    "ny_converted = ny.convert('jpg')\n",
    "for img in ny_converted.sequence:\n",
    "????page = ny(image = img)\n",
    "????page.save(filename='new york pdf to image.jpg')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "01c71419-e5f2-4e88-b3c0-99c72f6a5db3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
