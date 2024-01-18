{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d47ee684",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "=====CONTACT BOOK======\n",
      "1. ADD CONTACT\n",
      "2. VIEW CONTACT LIST\n",
      "3. SEARCH A CONTACT\n",
      "4. UPDATE A CONTACT\n",
      "5. DELETE A CONTACT\n",
      "6. EXIT\n"
     ]
    }
   ],
   "source": [
    "contacts=[]\n",
    "while True:\n",
    "    print(\"\\n=====CONTACT BOOK======\")\n",
    "    print(\"1. ADD CONTACT\")\n",
    "    print(\"2. VIEW CONTACT LIST\")\n",
    "    print(\"3. SEARCH A CONTACT\")\n",
    "    print(\"4. UPDATE A CONTACT\")\n",
    "    print(\"5. DELETE A CONTACT\")\n",
    "    print(\"6. EXIT\")\n",
    "\n",
    "    c = input(\"Enter your choice: \")\n",
    "\n",
    "    if c == '1':\n",
    "        name = input(\"Enter name: \")\n",
    "        phone_number = input(\"Enter phone number: \")\n",
    "        email = input(\"Enter email: \")\n",
    "        address = input(\"Enter address: \")\n",
    "        contact = {'name': name, 'phone_number': phone_number, 'email': email, 'address': address}\n",
    "        contacts.append(contact)\n",
    "        print(f\"\\nContact added successfully for {name}.\")\n",
    "    \n",
    "    elif c == '2':\n",
    "        print(\"\\nContact List:\")\n",
    "        for idx, contact in enumerate(contacts, start=1):\n",
    "             print(f\"{idx}. Name: {contact['name']} - Phone Number: {contact['phone_number']}\")\n",
    "\n",
    "    elif c == '3':\n",
    "         keyword = input(\"Enter name or phone number to search: \")\n",
    "         results = [contact for contact in contacts if keyword.lower() in contact['name'].lower() or keyword in contact['phone_number']]\n",
    "         print(\"\\nSearch Results:\")\n",
    "         for idx, result in enumerate(results, start=1):\n",
    "                print(f\"{idx}. Name: {result['name']} - Phone Number: {result['phone_number']}\")\n",
    "                \n",
    "    elif c == '4':\n",
    "          index = int(input(\"Enter the index of the contact to update: \")) - 1\n",
    "          if 0 <= index < len(contacts):\n",
    "             name = input(\"Enter updated name: \")\n",
    "             phone_number = input(\"Enter updated phone number: \")\n",
    "             email = input(\"Enter updated email: \")\n",
    "             address = input(\"Enter updated address: \")\n",
    "             contacts[index] = {'name': name, 'phone_number': phone_number, 'email': email, 'address': address}\n",
    "             print(\"Contact updated successfully.\")\n",
    "          else:\n",
    "              print(\"Invalid index. Please try again.\")\n",
    "              \n",
    "    elif c == '5':\n",
    "         index = int(input(\"Enter the index of the contact to delete: \")) - 1\n",
    "         if 0 <= index < len(contacts):\n",
    "             deleted_contact = contacts.pop(index)\n",
    "             print(f\"Contact deleted successfully: {deleted_contact['name']}.\")\n",
    "         else:\n",
    "             print(\"Invalid index. Please try again.\")\n",
    "\n",
    "    elif c == '6':\n",
    "        print(\"Exiting the Contact Management System. Goodbye!\")\n",
    "        break\n",
    "    else:\n",
    "        print(\"Invalid choice. Please enter a number between 1 and 6.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3bdde925",
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
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
