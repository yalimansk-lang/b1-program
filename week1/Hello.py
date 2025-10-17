{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "bb00327c-54c7-4566-a893-452a8d48d846",
   "metadata": {},
   "outputs": [
    {
     "ename": "_IncompleteInputError",
     "evalue": "incomplete input (2371873274.py, line 1)",
     "output_type": "error",
     "traceback": [
      "  \u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[3]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[31m    \u001b[39m\u001b[31m'''Business Profit CalculatorCalculates profit and margin percentagefrom revenue and cost data’’’\u001b[39m\n    ^\n\u001b[31m_IncompleteInputError\u001b[39m\u001b[31m:\u001b[39m incomplete input\n"
     ]
    }
   ],
   "source": [
    "'''Business Profit CalculatorCalculates profit and margin percentagefrom revenue and cost data’’’\n",
    "\n",
    "# Get revenue from user\n",
    "\n",
    "revenue = float(input(\"Enter total revenue: $\"))\n",
    "# Get costs from user  \n",
    "\n",
    "costs = float(input(\"Enter total costs: $\"))\n",
    "\n",
    "# Calculate profit\n",
    "\n",
    "profit = revenue – costs\n",
    "\n",
    "# Calculate profit margin percentage\n",
    "\n",
    "margin = (profit / revenue) * 100\n",
    "\n",
    "# Display results\n",
    "\n",
    "print(\"\\n--- Financial Summary ---\")\n",
    "print(f\"Revenue: ${revenue:,.2f}\")\n",
    "print(f\"Costs: ${costs:,.2f}\")\n",
    "print(f\"Profit: ${profit:,.2f}\")\n",
    "print(f\"Profit Margin: {margin:.1f}%\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "3f384734-2727-49bf-97c4-ebe4e5f037db",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Type help() for interactive help, or help(object) for help about object."
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "help\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "07d30afa-2e1c-46f3-bffd-27b868ee6f9b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Welcome to Python 3.14's help utility! If this is your first time using\n",
      "Python, you should definitely check out the tutorial at\n",
      "https://docs.python.org/3.14/tutorial/.\n",
      "\n",
      "Enter the name of any module, keyword, or topic to get help on writing\n",
      "Python programs and using Python modules.  To get a list of available\n",
      "modules, keywords, symbols, or topics, enter \"modules\", \"keywords\",\n",
      "\"symbols\", or \"topics\".\n",
      "\n",
      "You can use the following keyboard shortcuts at the main interpreter prompt.\n",
      "F1: enter interactive help, F2: enter history browsing mode, F3: enter paste\n",
      "mode (press again to exit).\n",
      "\n",
      "Each module also comes with a one-line summary of what it does; to list\n",
      "the modules whose name or summary contain a given string such as \"spam\",\n",
      "enter \"modules spam\".\n",
      "\n",
      "To quit this help utility and return to the interpreter,\n",
      "enter \"q\", \"quit\" or \"exit\".\n",
      "\n"
     ]
    }
   ],
   "source": [
    "help()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "80752257-7b3b-47c1-96f6-b5ea038d7415",
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
   "version": "3.14.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
