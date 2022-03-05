r"""
We use the following notation to describe the gradient-boosted trees formulation:

.. math::

    \begin{align*}
    T &:= \text{Set of trees in ensemble}\\
    L_t &:= \text{Set of leaves in tree $t$}\\
    z_{t,l} &:= \text{Binary variable indicating if leaf $l$ in
        tree $t$ is active}\\
    \text{Left}_{t,s} &:= \text{Set of leaf variables left of split $s$
        in tree $t$}\\
    \text{Right}_{t,s} &:= \text{Set of leaf variables right of split $s$
        in tree $t$}\\
    y_{i(s),j(s)} &:= \text{Binary variable indicating if split $s$ is active
        (i.e. $i(s)$ and $j(s)$ are feature and index of split $s$,
        respectively)}\\
    V_t &:= \text{Set of splits in tree $t$}\\
    n &:= \text{Index set of input features}\\
    m_i &= \text{Index set of splits for feature $i$}\\
    F_{t,l} &= \text{Weight of leaf $l$ in tree $t$}\\
    \end{align*}
"""
from omlt.gbt.gbt_formulation import GBTBigMFormulation
from omlt.gbt.model import GradientBoostedTreeModel
