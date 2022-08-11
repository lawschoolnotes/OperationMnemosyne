#! usr/bin/env/python3
# @author: tecumseh


"""Class to create a terminal prompt for LSN project"""
#%%
from prompt_toolkit import PromptSession, prompt, HTML, Application
from prompt_toolkit.shortcuts import radiolist_dialog
from prompt_toolkit import print_formatted_text as print

class Prompts(list):
    
    def __init__(self, call_results: list):
        self.call_results = call_results
        
    def _responseparse(self):
        count = self.call_results['count']
        responseResults = self.call_results['results']
        pick_result = [r['name'] for r in responseResults]
        result_len = ["kw"+ str(i) for i in range(len(pick_result))]
        values = list(zip(result_len, pick_result))
        self.values = values
        return self.values
    
    def Sessionmain():
        session = PromptSession()
        
        while True:
            try:
                text = session.prompt('> ')
            except KeyboardInterrupt:
                continue
            except EOFError:
                break
            else:
                print('You entered:', text)
    
    def createRadioDialog(self, title_text: str, body_text: str):
        """Function to create the terminal prompt

        Args:
            title_text (str): Text to appear as the title of the prompt.
            body_text (str): Question with which to prompt the user.
        """
        self.title_text = title_text
        self.body_text = body_text
        self._responseparse()
        prompt = radiolist_dialog(
            title=f'{title_text}',
            text=f'{body_text}',
            values= self.values).run()
    def main():
        app = Application(full_screen=True)
# %%
#%% Test this thing out

if __name__ =='__main__':
    main()
    