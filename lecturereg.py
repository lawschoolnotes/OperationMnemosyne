import re

class TextFormatter:
    """Class to format a text file with regular expressions.
    
    Args:
        text_in (str): Input file path as string.
        text_out (str): Output file path as string;
                        can be same as text_in, 
                        but will overwrite source.

    """
    def __init__(self, text_in, text_out):
        self.text_in = text_in
        self.text_out = text_out
        
        if self.text_out == self.text_in:
            with open(self.text_in, 'r', encoding='utf-8') as f:
                self.text = f.read()
            return print(f"CAUTION: {self.text_out} content will be overwritten")
        else:
            with open(self.text_in, 'r', encoding='utf-8') as f:
                self.text = f.read()
            return print(f"{self.text_out} will be created if it does not exist.")
                
    def regtext(self, regstring, sub=""):
        """Use a regular expression to edit a text file

        Args:
            regstring (str): regular expression as string
            sub (str): String to replace match groups.
                       Default is a blank string, 
                       which deletes the matching groups.
        """
        test_str = self.text
        regex = rf"{regstring}"
        resulttup = re.subn(regex, sub, test_str, 0, re.MULTILINE)
        result = resulttup[0]
        subs = resulttup[1]
        if self.text_out == self.text_in:
            with open(self.text_in, 'w', encoding='utf-8') as f:
                f.write(result)
            return print(f'{subs} substitutions made in {self.text_in}.')
        else:
            with open(self.text_out, 'w', encoding='utf-8') as j:
                j.write(result)
            return print(f'{subs} substitutions made to {self.text_in} and written to {self.text_out}.')

