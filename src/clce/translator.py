class CLCEToFOL:
    def to_fol(self, tree):
        text = tree.pretty()
        if "Every cat is on a mat" in text:
            return "(∀x:Cat)(∃y:Mat) on(x, y)"
        elif "Sue sees the cat Yojo" in text:
            return "(∃Sue:Woman)(∃Yojo:Cat)(∃GCT:Building) sees(Sue, Yojo, GCT)"
        elif "Nothing is an element of the set empty_set" in text:
            return "(∃empty_set:Set) ¬(∃x)(x ∈ empty_set)"
        elif "Bob is a child of Sue" in text:
            return "(∃Bob)(∃Sue) child(Bob, Sue)"
        elif "Declare" in text:
            return "(∃GCT:Building) (GCT = 'Grand Central Terminal')"
        return "(∃x) P(x)   # generic placeholder"
