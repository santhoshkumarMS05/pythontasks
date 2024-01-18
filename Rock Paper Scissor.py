{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1c23602b",
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "print(\"---Rock, Paper, Scissors Game---\")\n",
    "user_point=0\n",
    "computer_point=0\n",
    "while True:\n",
    "    user=input(\"Choose any one rock,paper,scissor:\")\n",
    "    computer=random.choice(['rock','paper','scissor'])\n",
    "    print(\"User choice:\",user)\n",
    "    print(\"Computer choice:\",computer)\n",
    "    if user in ['rock','paper','scissor']:\n",
    "        if user == computer:\n",
    "            result=\"It's a tie!\"\n",
    "            print(result)\n",
    "        elif user =='rock' and computer=='scissors':\n",
    "            result=\"you win!\"\n",
    "            print(result)\n",
    "        elif user=='paper' and computer=='rock':    \n",
    "            result=\"you win!\"\n",
    "            print(result)\n",
    "        elif user=='scissors' and computer=='paper':  \n",
    "            result=\"you win!\"\n",
    "            print(result)\n",
    "        else:\n",
    "            result=\"computer wins!\"\n",
    "            print(result)\n",
    "    else:\n",
    "        result=\"please enter the valid choice!\"\n",
    "        print(result)\n",
    "    if result==\"you win!\":\n",
    "        user_point=user_point+1\n",
    "    if result==\"computer wins!\":\n",
    "        computer_point=computer_point+1\n",
    "    print(\"user point:\",user_point)\n",
    "    print(\"computer point:\",computer_point)\n",
    "    play= input(\"\\nDo you want to play again? (yes/no): \")\n",
    "    if play != 'yes':\n",
    "        print(\"\\nThank you for playing!\")\n",
    "        break"
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
