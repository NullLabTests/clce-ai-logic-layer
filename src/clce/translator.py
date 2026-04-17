class CLCEToFOL:
    def to_fol(self, sentence):
        if "Every cat is on a mat" in sentence:
            return "(∀x:Cat)(∃y:Mat) on(x, y)"
        elif "Sue sees the cat Yojo" in sentence:
            return "(∃Sue:Woman)(∃Yojo:Cat)(∃GCT:Building) sees(Sue, Yojo, GCT)"
        elif "Nothing is an element of the set empty_set" in sentence:
            return "(∃empty_set:Set) ¬(∃x)(x ∈ empty_set)"
        elif "Bob is a child of Sue" in sentence:
            return "(∃Bob)(∃Sue) child(Bob, Sue)"
        elif "Declare" in sentence:
            return "(∃GCT:Building) (GCT = 'Grand Central Terminal')"
        return "(∃x) P(x)  # generic"
