{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5784a0d1",
   "metadata": {},
   "outputs": [],
   "source": [
    "num1 = int(input(\"Enter the first number: \"))\n",
    "num2 = int(input(\"Enter the second number: \"))\n",
    "print(\"Enter the operation to be performed:\")\n",
    "print(\"1. ADDITION\\n2. SUBTRACTION\\n3. MULTIPLICATION\\n4. DIVISION\")\n",
    "n = int(input())\n",
    "\n",
    "if n == 1:\n",
    "    result = num1 + num2\n",
    "    print(\"The Addition of the two numbers:\", result)\n",
    "elif n == 2:\n",
    "    result = num1 - num2\n",
    "    print(\"The Subtraction of the two numbers:\", result)\n",
    "elif n == 3:\n",
    "    result = num1 * num2\n",
    "    print(\"The Multiplication of the two numbers:\", result)\n",
    "elif n == 4:\n",
    "    if num2 != 0:\n",
    "        result = num1 / num2\n",
    "        print(\"The Division of the two numbers:\", result)\n",
    "    else:\n",
    "        print(\"Division by zero is not allowed\")\n",
    "else:\n",
    "    print(\"Invalid input for operation\")\n"
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
