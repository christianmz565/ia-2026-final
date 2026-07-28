#import "els-globals.typ": *
#import "els-utils.typ": *

#let default-author = (
  name: none,
  affiliation: none,
  corr: none,
  id: "a"
)

#let make-author(author) = box({
  author.name

  let auth-affiliation = if author.at("affiliations", default: none) == none {
    none
  } else {
    author.affiliations.map((key) => {key})
  }

  let auth-rest
  let iscorr
  if author.at("corresponding", default: false) == true {
      auth-rest = (sym.ast,)
      iscorr = true
    } else {
      auth-rest = none
      iscorr = false
    }

  if iscorr or auth-affiliation != none {
    sym.space.thin
    super(typographic: false, (auth-affiliation + auth-rest).join([,]))
  }
})

#let make-authors(authors) = par({
  set text(size: font-size.author)
  authors.map(make-author).join(", ", last: " and ")
})

#let make-author-meta(authors) = {
  let names = ()

  if authors.len() == 0 {return ()}

  for author in authors {
    if type(author.name) == content {
      names.push(author.name.text)
    } else {
      names.push(author.name)
    }
  }
  return names.join(" ")
}

#let make-corresponding-author(authors, els-columns, lang: "es") = {
  let corr-authors = authors.filter(a => a.at("corresponding", default: false) == true)
  if corr-authors.len() == 0 { return }

  place(
    float: true,
    bottom,
    {
      v(0.5em)
      let line-length = if els-columns == 1 {9.6em} else {4.6em}
      line(length: line-length, stroke: 0.25pt)
      v(-0.75em)
      set text(size: 10pt)
      set par(leading: 0.5em)
      let label = if lang == "en" {
        if corr-authors.len() == 1 [Corresponding author.] else [Corresponding authors.]
      } else {
        if corr-authors.len() == 1 [Autor correspondiente.] else [Autores correspondientes.]
      }
      [#h(1em);#super[#sym.ast]#h(0.1em);#label]
      for author in corr-authors {
        let email = if author.at("email", default: none) != none {author.email} else {"No email provided"}
        linebreak()
        h(1.4em)
        let email-label = if lang == "en" { "Email: " } else { "Correo electrónico: " }
        [#email-label #email]
      }
    }
  )
}

#let make-affiliation(key, value) = {
  super[#key]
  if key != " " {
    sym.space.thin
  }
  text(style:"italic", value)
}

#let make-affiliations(affiliations) = {
  for (key, value) in affiliations{
    make-affiliation(key, value)
    linebreak()
  }
}

#let make-title(title: none, authors: (), affiliations: ()) = align(center, {
  par(leading: 0.95em, text(size: font-size.title, title))
  v(0.9em)
  text(size: font-size.author, make-authors(authors))
  v(0.2em)
  par(leading: 0.65em, text(size: font-size.small, make-affiliations(affiliations), top-edge: 0.5em))
  v(1.75em)
})

// Format the abstract
#let make-abstract(abstract, keywords, els-format, lang: "es") = if abstract != none {
    let abstract-label = if lang == "en" { "Abstract" } else { "Resumen" }
    let keywords-label = if lang == "en" { "Keywords: " } else { "Palabras clave: " }
    set par(justify: true)
    line(length: 100%, stroke: 0.5pt)
    v(-0.25em)
    text(weight: "bold")[#abstract-label]
    if els-format.type.contains("review") {v(0.5em)} else {v(-0.2em)}
    abstract
    if els-format.type.contains("review") {linebreak()} else {v(0em)}
    if keywords != () {
      let kw = ()
      for keyword in keywords{
        kw.push(keyword)
      }

    let kw-string = if kw.len() > 1 {
        kw.join(", ")
      } else {
        kw.first()
      }
      text((emph(keywords-label), kw-string).join())
    }
    v(-0.2em)
    line(length: 100%, stroke: 0.5pt)
    if els-format.type.contains("review") {v(-0.75em)}
    else if els-format.type.contains("5p") {v(-0.25em)}
    else {none}
}
