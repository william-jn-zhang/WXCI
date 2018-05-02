from docx import Document

class NamelistDocxReader:

    param_skip_row_num_head = 6
    param_skip_row_num_tail = 1
    param_extract_cols = [0, 1, 3]

    def extract(self, docxfile):
        document = Document(docxfile)
        tables = document.tables
        res = []
        for t in tables:
            for i in range(self.param_skip_row_num_head, len(t.rows) - self.param_skip_row_num_tail):
                l = []
                for e in self.param_extract_cols:
                    l.append(t.row_cells(i)[e].text)
                if l[0] == "":
                    continue
                res.append(l)
        return res

if __name__ == "__main__":
    nl = NamelistDocxReader()
    res = nl.extract("namelist.docx")
    print(res)
    print(len(res))
