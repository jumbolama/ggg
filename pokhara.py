{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import csv\n",
    "url=\"https://www.timeanddate.com/\"\n",
    "\n",
    "def get_data(url, trail_url,):\n",
    "    response = requests.get(url+trail_url)\n",
    "    soup = BeautifulSoup(response.content, 'lxml')\n",
    "    classes = soup.find_all(\"table\")\n",
    "    table = classes[0]\n",
    "    raw_trs = table.find_all(\"tr\")\n",
    "    clean_trs = raw_trs[1:18]\n",
    "    raw_columns, raw_rows = clean_trs[0], clean_trs[1:]\n",
    "    columns = [th.text.strip().replace(\"\\xa0\",\"\").replace(\"\",\"\") for th in raw_columns.find_all(\"th\")]  \n",
    "    rows = [[td.text.strip().replace(\"\\xa0\",\"\").replace(\"↑\",\"\") for td in row.find_all([\"th\",\"td\"])] for row in raw_rows]    \n",
    "    return columns, rows\n",
    "\n",
    "def get_dict(**datas):\n",
    "    columns = datas.get('columns')\n",
    "    rows = datas.get('rows')\n",
    "    return [dict(zip(columns, row)) for row in rows]\n",
    "\n",
    "def write_to_csv(filename,datas):\n",
    "    with open(filename, 'w') as write_file:\n",
    "        writer = csv.DictWriter(write_file, fieldnames=datas[0].keys())\n",
    "        writer.writeheader()\n",
    "        writer.writerows(datas)\n",
    "        \n",
    "\n",
    "columns, rows = get_data(url, 'weather/nepal/pokhara/ext')\n",
    "datas = get_dict(columns=columns, rows=rows)\n",
    "write_to_csv(\"Pokhara_weather\",datas)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "less Pokhara_weather.csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
