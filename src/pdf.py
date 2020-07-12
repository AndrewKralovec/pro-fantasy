import sys
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle


def main(file_name, table):
    (headers, data) = table
    data.insert(0, headers)
    (w, h) = letter
    l = (w + (len(data[0]) * 3) * 15, h + len(data) * 15)
    doc = SimpleDocTemplate(file_name, pagesize=l)
    # container for the 'Flowable' objects
    elements = []

    t = Table(data, len(data[0])*[0.85*inch], len(data)*[0.85*inch])
    t.setStyle(TableStyle([('LINEABOVE', (0, 0), (-1, 0), 2, colors.green),
                           ('LINEABOVE', (0, 1), (-1, -1), 0.25, colors.black),
                           ('LINEBELOW', (0, -1), (-1, -1), 2, colors.green),
                           ('ALIGN', (1, 1), (-1, -1), 'RIGHT')]))

    elements.append(t)
    # Write the document to disk
    doc.build(elements)
    return ('done')


if __name__ == "__main__":
    print(main(sys.argv[1:]))
