## model1.py
    - it reads the files of english and foreign corpus
    - stores the english and foreign sentences pairwise in list of list
    - initialising the translation probabilities
    - Applying EM algorithm to find the alignment of english with foreign word in particular sentences

## ibm.py

    - IBM Model 1 Lexical translation model that ignores word order.

    - In IBM Model 1, word order is ignored for simplicity. As long as the word alignments are equivalent, it doesn't matter where the word occurs in the source or target sentence. so the alignments are equally likely.

        Source: du jambon je mange
        Target: eat i some ham
        Alignment: (0,3) (1,2) (2,0) (3,1)

    - IBM Model 2 Lexical translation model that considers word order.

    - IBM Model 2 improves on Model 1 by accounting for word order. An alignment probability is introduced, a(i | j,l,m), which predicts a source word position, given its aligned target word's position.

## phrase.py

    - It uses phrase-based translation model to translate french sentences into english sentences.
    - It uses alignments obtained by our IBM Model 1 implementation as inputs.
    - Phrase extraction algorithm extracts all consistent phrase pairs from a word-aligned sentence pair.
    - We used all these pairs to calculate scores for each extracted phrase and rank them in order of descending probability.
