from typing import Dict, Any, Union


def user_prompt_choose_dict(
        d=None,
        prompt: str = "Please choose:",
        quitkey: str = 'q',
        invalidmsg: str = "Invalid choice.",
        showvalidchoices: bool = True
) -> Union[Any, None]:
    if d is None:
        d = {1: 'apple', '2': 'banana', 3: 'potato'}

    while True:
        for k in d.keys():
            v = d[k]
            print("- [{:^3s}] {}".format(k, repr(v)))
        selection = input(
            prompt +
            (" ({} to quit)".format(quitkey) if quitkey else '') +
            "\n > "
        )
        if quitkey and (selection == quitkey):
            return None

        if selection in d.keys():
            # if they choose a valid choice
            return d[selection]
        else:
            print(invalidmsg)

            if showvalidchoices:
                print("Valid choices: {}".format(repr(list(d.keys()))))


def user_prompt_yn(prompt: str = "Yes or no?", promptdict=None, successval="Yes") -> bool:

    if promptdict is None:
        promptdict = {'y': successval, 'n': "No"}

    daChoice = user_prompt_choose_dict(promptdict, prompt)

    return daChoice == successval
