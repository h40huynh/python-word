class Style:
    @staticmethod
    def ParagraphStyle(style: str):
        return style.strip()

    @staticmethod
    def CharStyle(style: str):
        return "{} Char".format(style.strip())

    @staticmethod
    def HeadingBySeverity(severity: str):
        return "{} heading".format(severity.strip())
