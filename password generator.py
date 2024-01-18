{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ceba7110",
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "chars=\"qwertyuiop[]asdfghjkl;'zxcvbnm,./QWERTYUIOP{}|ASDFGHJKL:ZXCVBNM<>?!@*1234567890_+-=#\"\n",
    "print(\"Welcome to the password generator!\")\n",
    "try:\n",
    " len=int(input(\"Enter the length of the password:\"))\n",
    " if len<=0:\n",
    "     print(\"Enter the correct length for the password generator!\")\n",
    " else:    \n",
    "  password=\"\"\n",
    "  for x in range(0,len):\n",
    "   char=random.choice(chars)\n",
    "   password=password+char\n",
    "  print(\"Here your password is :\",password)\n",
    "except ValueError:\n",
    "    print(\"Please enter the valid input for the password generator\")"
   ]
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
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
