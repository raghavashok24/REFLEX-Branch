# Theorem 4: the Pigouvian wedge

The externality formalized rather than narrated. This is the section an EconML
reviewer looks for after reading the framing, and its absence is what would make
the paper read as an ML paper wearing economics vocabulary.

## The welfare object

In the stable regime the market's common mode is an AR(1) with coefficient
`-m_N` driven by noise, so its stationary variance is proportional to

```
   V(m_N)  =  sigma^2 / (1 - m_N^2) ,
```

a smooth welfare cost diverging as the market approaches its boundary. This is
the paper's price of instability, and it is a modeling choice that gets defended
in the text rather than asserted: stationary variance is the smooth proxy for
divergence risk, it is finite everywhere inside the stable region, and it
diverges exactly at the boundary the rest of the paper is about.

## The private problem

Let each firm choose an adaptation aggressiveness `a_i`, meaning cadence,
learning rate, or responsiveness, anything scaling its contribution to `m_1`.
Aggressiveness buys tracking benefit `B(a_i)`, concave. The variance cost is
shared: firm `i` bears its own exposure while its marginal contribution to
`m_N` raises everyone's, plus the client-side exposure it does not bear at all.

```
   private:  max_{a_i}  B(a_i)  -  w_i * V( m_N(a_1, ..., a_N) )
   social:   max_{a}    sum_i B(a_i)  -  W * V( m_N(a) )      ,   W  >  sum_i w_i
```

## Statement

**Theorem 4.** At a symmetric equilibrium the private first-order condition
ignores the fraction `(N-1)/N` of the marginal variance cost borne by other
firms, plus the entire client-side exposure. The corrective fee equals the
externalized marginal cost

```
   t*  =  ( d m_N / d a_i ) * ( d/d m_N ) [ variance cost borne by others ]
```

which is closed form given `V`, and is increasing in `N`, in `kappa`, and
steeply in proximity to the boundary, since

```
   dV/dm_N  =  2 sigma^2 m_N / (1 - m_N^2)^2 .
```

**Corollary (over-adaptation).** The decentralized equilibrium over-adapts
relative to the social optimum for every `N >= 2`, with the distortion growing
as the market crowds. [DERIVED]

## What the merge adds

`d m_N / d a_i` decomposes into two channels, because `m_N = m_1 N_eff` and
`N_eff` depends on `s`:

```
   aggressiveness channel:   d m_N / d a_i  through  m_1
   provenance channel:       d m_N / d s    =  m_1 * kappa * (N - 1)
```

The same wedge therefore prices **shared-model adoption** directly, which turns
the monoculture externality into a fee rather than a warning, and connects this
result to the adoption-incentive question the call for papers asks about.
[DERIVED]

Note the provenance channel is linear in `N` and does not decay: a firm's
decision to adopt the market-leading vendor imposes a marginal cost on the
market that grows with market size, while its private quality gain does not.
That asymmetry is the reason unregulated adoption dynamics run toward the
unstable configuration rather than away from it.

## The policy triple

This is where the paper's three levers are named as what they are, which is the
standard instrument taxonomy. Say it in one sentence and an economics reader
knows exactly what they are looking at.

| Lever | Instrument type | Where |
|---|---|---|
| Cadence caps | Quantity regulation | Theorem 2 |
| Correction mandates | Technology mandate | Theorem 3 |
| Diversity floors | Structural remedy | Theorem 3 |
| The wedge | Price instrument | Theorem 4 |

The quantity-versus-price choice under uncertainty is Weitzman's question, and
the paper cites it for the framing rather than solving it. Worth one sentence,
because a reader from economics will otherwise supply the objection themselves.

## Open items

1. Write the welfare page: benefit function, both first-order conditions, the
   wedge, the over-adaptation proof. One page. [TO BUILD]
2. Confirm the AR(1) reduction of the common mode gives exactly
   `1/(1 - m_N^2)`, including the sign convention on `-m_N`. It should, since
   the variance depends on the square, but certify it rather than assert it.
   [TO BUILD]
3. Decide whether `W > sum_i w_i` (client-side exposure) needs a microfoundation
   or can be an assumption with one sentence of justification. Leaning
   assumption; the result does not depend on its size, only its sign.
4. Experiment 6 is decentralized against socially optimal aggressiveness on a
   small grid, plus the wedge's comparative statics in `N`, `kappa` and `s`.
   Second in the de-scope order; if cut, Theorem 4 ships as theory.
