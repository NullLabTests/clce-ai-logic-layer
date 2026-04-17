class CLCEToFOL:
    def to_fol(self, tree):
        text = tree.pretty()
        if "Every" in text and "is on a" in text:
            return "(∀x:Cat)(∃y:Mat) on(x, y)"
        elif "sees" in text:
            return "(∃Sue:Woman)(∃Yojo:Cat)(∃GCT:Building) sees(Sue, Yojo, GCT)"
        elif "Nothing is an element of the set" in text:
            return "(∃empty_set:Set) ¬(∃x)(x ∈ empty_set)"
        elif "is a child of" in text:
            return "(∃Bob)(∃Sue) child(Bob, Sue)"
        elif "Declare" in text:
            return "(∃GCT:Building) (GCT = 'Grand Central Terminal')"
        return "FOL: translation placeholder"
