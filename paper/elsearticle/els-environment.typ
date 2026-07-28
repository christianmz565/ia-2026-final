#import "els-globals.typ": *

// Appendix
#let appendix(body, lang: "es") = {
  let appendix-supplement = if lang == "en" { [Appendix] } else { [Apéndice] }
  set heading(numbering: "A.1.", supplement: appendix-supplement)
  // Reset heading counter
  counter(heading).update(0)

  // Equation numbering
  let numbering-eq = (..n) => {
    let h1 = counter(heading).get().first()
    numbering("(A.1a)", h1, ..n)
  }
  set math.equation(numbering: numbering-eq)

  // Figure and Table numbering
  let numbering-fig = n => {
    let h1 = counter(heading).get().first()
    numbering("A.1", h1, n)
  }

  set figure(numbering: numbering-fig)

  isappendix.update(true)

  body
}