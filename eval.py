import subprocess
import collections

def run_command(command):
    try:
        output = subprocess.check_output(command, shell=True, text=True)
        return output
    except subprocess.CalledProcessError as e:
        print("error happened:", e)
        return None

if __name__ == "__main__":
    # command
    #command = "cat all_four.txt | apertium -d . jpn-segment | hfst-proc jpn.automorf.hfst | cg-proc -w jpn.rlx.bin"
    command = "cat all_four.txt | apertium -d . jpn-disam"
    
    # command execution
    result = run_command(command)

    # stats
    if result is not None:
        a = result.split()
        b = len(a)
        unknownTokens = collections.Counter(filter(lambda x:'*' in x, result))
        unknown_count = sum(unknownTokens.values())
        coverage = (1 - unknown_count / b) * 100
        print("total words:"+str(b))
        print("unknown words:"+str(unknown_count))
        print(f"coverage: {coverage:.2f}%")
        # print(b-unknownTokens/b ** 100 + "%")
