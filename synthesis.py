from synthesis_options import SynthesisOption, SynthesisOptionType




ID = "de.cau.cs.kieler.plyghd.PlyghdKgraphSynthesis"

COLOR = SynthesisOption("de.cau.cs.kieler.plyghd.PlyghdKgraphSynthesis.color", "Color", SynthesisOptionType.TEXT, "0x000000")
LABELS = SynthesisOption("de.cau.cs.kieler.plyghd.PlyghdKgraphSynthesis.labels", "Labels", SynthesisOptionType.CHECK, True)


class PlyghdKgraphSynthesis:
    def getDisplayedSynthesisOptions(self):
        return [COLOR, LABELS]
    
    def transform(self, graph):
        pass