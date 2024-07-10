from graphviz import Digraph
#############Intoductory Functions##################################################


###################Graph Functions"""""""""""""""""""""""""""""""""""

def DFC_based_on_Origins ( dot, driver):
    dot.attr("node", shape="circle", fixedsize="false", width="0.4", height="0.4", fontname="Helvetica",
             fontsize="8", margin="0")




    dot.node("a", str("a"), color="#000000", style="filled",
                     fillcolor="#ffc000"         )
    dot.node("b", str("b"), color="#000000", style="filled",
                     fillcolor="#ffc000"         )

    dot.edge("a", "b", style="dashed", arrowhead="none",
                     color="#000000")


