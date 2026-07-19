{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "367a8b21-997c-45b7-96c7-ec437b208bb6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "          id      cuisine                                        ingredients\n",
      "0      10259        greek  [romaine lettuce, black olives, grape tomatoes...\n",
      "1      25693  southern_us  [plain flour, ground pepper, salt, tomatoes, g...\n",
      "2      20130     filipino  [eggs, pepper, salt, mayonaise, cooking oil, g...\n",
      "3      22213       indian                [water, vegetable oil, wheat, salt]\n",
      "4      13162       indian  [black pepper, shallots, cornflour, cayenne pe...\n",
      "...      ...          ...                                                ...\n",
      "39769  29109        irish  [light brown sugar, granulated sugar, butter, ...\n",
      "39770  11462      italian  [KRAFT Zesty Italian Dressing, purple onion, b...\n",
      "39771   2238        irish  [eggs, citrus fruit, raisins, sourdough starte...\n",
      "39772  41882      chinese  [boneless chicken skinless thigh, minced garli...\n",
      "39773   2362      mexican  [green chile, jalapeno chilies, onions, ground...\n",
      "\n",
      "[39774 rows x 3 columns]\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "df = pd.read_json(r'train.json')\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f9f4af15-d65b-4572-b39a-6923157a9c5e",
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
   "version": "3.14.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
