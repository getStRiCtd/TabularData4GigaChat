import datasets

def load_tab_fact():
    return datasets.load_dataset("ibm-research/tab_fact")

def load_fetaqa():
    return datasets.load_dataset("DongfuJiang/FeTaQA")

def load_wikitq():
    return datasets.load_dataset("Stanford/wikitablequestions")