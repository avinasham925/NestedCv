{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8856a771-7969-4fe9-a490-a8c85b8801f4",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "expected an indented block after function definition on line 9 (3652878348.py, line 14)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[1], line 14\u001b[1;36m\u001b[0m\n\u001b[1;33m    if __name__ == \"__main__\":\u001b[0m\n\u001b[1;37m                              ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m expected an indented block after function definition on line 9\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "59b6f80c-ce5c-416a-9428-4b2f9a2bb094",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'df' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[3], line 37\u001b[0m\n\u001b[0;32m     34\u001b[0m gts \u001b[38;5;241m=\u001b[39m GroupedTimeSeriesSplit(n_splits\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m5\u001b[39m)\n\u001b[0;32m     36\u001b[0m \u001b[38;5;66;03m# Example of how to use the custom cross-validator\u001b[39;00m\n\u001b[1;32m---> 37\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m train_index, test_index \u001b[38;5;129;01min\u001b[39;00m gts\u001b[38;5;241m.\u001b[39msplit(\u001b[43mdf\u001b[49m):\n\u001b[0;32m     38\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mTrain indices:\u001b[39m\u001b[38;5;124m\"\u001b[39m, train_index)\n\u001b[0;32m     39\u001b[0m     \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mTest indices:\u001b[39m\u001b[38;5;124m\"\u001b[39m, test_index)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'df' is not defined"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sklearn.model_selection import BaseCrossValidator\n",
    "\n",
    "class GroupedTimeSeriesSplit(BaseCrossValidator):\n",
    "    def __init__(self, n_splits=5):\n",
    "        self.n_splits = n_splits\n",
    "\n",
    "    def split(self, X, groups=None):\n",
    "        day_col = 'day'  \n",
    "        month_col = 'month' \n",
    "        year_col = 'year'  \n",
    "\n",
    "        unique_years = X[year_col].unique()\n",
    "        unique_years.sort()\n",
    "\n",
    "        splits = []\n",
    "        current_idx = 0\n",
    "\n",
    "        for i in range(self.n_splits):\n",
    "            train_end_idx = int(len(unique_years) * (i + 1) / self.n_splits)\n",
    "\n",
    "            train_years = unique_years[current_idx:train_end_idx]\n",
    "            test_years = unique_years[train_end_idx:train_end_idx + 1]\n",
    "\n",
    "            train_indices = X[X[year_col].isin(train_years)].index.tolist()\n",
    "            test_indices = X[X[year_col].isin(test_years)].index.tolist()\n",
    "\n",
    "            yield train_indices, test_indices\n",
    "\n",
    "            current_idx = train_end_idx\n",
    "\n",
    "    def get_n_splits(self, X=None, y=None, groups=None):\n",
    "        return self.n_splits\n",
    "gts = GroupedTimeSeriesSplit(n_splits=5)\n",
    "\n",
    "# Example of how to use the custom cross-validator\n",
    "for train_index, test_index in gts.split(df):\n",
    "    print(\"Train indices:\", train_index)\n",
    "    print(\"Test indices:\", test_index)\n",
    "    print()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5d52264c-4748-4c64-837e-a5117c639aca",
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
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
