from object import Item
from lxml import html

class Parser:

    def parse_object(self, content):
        tree = html.fromstring(content)
        table = tree.xpath('/html/body/div[3]/div[2]/div[4]/div[2]/div[1]/div/div[3]/div/table/text()')

        answer = []

        for idx in range(3,len(table)):
            result = self.get_result(tree, idx)
            item = Item(
                date=self.get_date(tree, idx),
                time=self.get_time(tree, idx),
                place=self.get_place(tree, idx),
                teamName=self.get_teamName(tree, idx),
                scored=result[0],
                missed=result[1]
            )
            if item.teamName == ' ' or item.scored == ' ':
                continue
            answer.append(item)

        return answer

    def get_date(self, tree, idx):
        # Check the case of link
        answ = tree.xpath(f'/html/body/div[3]/div[2]/div[4]/div[2]/div[1]/div/div[3]/div/table/tr[{idx}]/td[2]/a/text()')
        if len(answ) == 0:
            answ = tree.xpath(f'/html/body/div[3]/div[2]/div[4]/div[2]/div[1]/div/div[3]/div/table/tr[{idx}]/td[2]/text()')
        if len(answ) == 0:
            return ' '

        return answ[0].strip()

    def get_time(self, tree, idx):
        # Check the case of link
        answ = tree.xpath(f'/html/body/div[3]/div[2]/div[4]/div[2]/div[1]/div/div[3]/div/table/tr[{idx}]/td[3]/a/text()')
        if len(answ) == 0:
            answ = tree.xpath(f'/html/body/div[3]/div[2]/div[4]/div[2]/div[1]/div/div[3]/div/table/tr[{idx}]/td[3]/text()')
        if len(answ) == 0:
            return ' '

        return answ[0].strip()

    def get_place(self, tree, idx):
        # Check the case of link
        answ = tree.xpath(f'/html/body/div[3]/div[2]/div[4]/div[2]/div[1]/div/div[3]/div/table/tr[{idx}]/td[4]/a/text()')
        if len(answ) == 0:
            answ = tree.xpath(f'/html/body/div[3]/div[2]/div[4]/div[2]/div[1]/div/div[3]/div/table/tr[{idx}]/td[4]/text()')
        if len(answ) == 0:
            return ' '

        return answ[0].strip()

    def get_teamName(self, tree, idx):
        # Check the case of link
        answ = tree.xpath(f'/html/body/div[3]/div[2]/div[4]/div[2]/div[1]/div/div[3]/div/table/tr[{idx}]/td[6]/a/text()')
        if len(answ) == 0:
            answ = tree.xpath(f'/html/body/div[3]/div[2]/div[4]/div[2]/div[1]/div/div[3]/div/table/tr[{idx}]/td[6]/text()')
        if len(answ) == 0:
            return ' '
            
        return answ[0].strip()

    def get_result(self, tree, idx):
        # Check the case of link
        answ = tree.xpath(f'/html/body/div[3]/div[2]/div[4]/div[2]/div[1]/div/div[3]/div/table/tr[{idx}]/td[7]/a/text()')
        if len(answ) == 0:
            answ = tree.xpath(f'/html/body/div[3]/div[2]/div[4]/div[2]/div[1]/div/div[3]/div/table/tr[{idx}]/td[7]/text()')
        if len(answ) == 0:
            return [' ',' ']

        answ = answ[0].strip()
        answ = answ.split()[0]
        numbers = []
        for word in answ.split(':'):
           if word.isdigit():
              numbers.append(int(word))

        if len(numbers) <= 1:
            return [' ',' ']

        return numbers