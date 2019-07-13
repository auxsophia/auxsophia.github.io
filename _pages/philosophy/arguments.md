---
layout: default
title: Philosopher Scholar - Arguments
permalink: /philosophy/arguments/
datatable: true
---

For more information on argumentation specific to [global warming](/globalWarming/), please see my resources on [global warming denialism](/philosophy/globalWarmingDenialism/).

I'm trying a different kind of project. I often debate with people over the internet and use many of the same arguments over and over. Instead of wasting time and energy reconstructing arguments, I want to write well thought out arguments to be copied and pasted as needed. This will also put my reasoning on public display, so anyone can criticize it. Hopefully I'll be less likely to fall into poor reasoning. I'll also be able to see how my views change over time.

In some cases, I may try to give a very brief version of the argument followed by a more in depth one, so I can use either depending on the situation. I will update as the arguments arise along with free time.

<html>
  <head>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
  </head>
  <body>
    <div id="headerContent"></div>

    <div class="container">
      <input type="text" id="myInput" onkeyup="argFunction()" placeholder="Search arguments...">

      <table id="argTable">
        <tr class="header">
          <th style="width:100%;">Argument</th>
        </tr>
        <tr>
          <td>
            Key terms: <br>
            Can you prove god doesn't exist? argument from ignorance
            <br>
            <br>
            Short argument:
            <br>
            The argument really is: if you cannot prove god does not exist, there remains a possibility that there is a god. This is true of any gods or supernatural beings, even the Greek gods. It's very hard to disprove this to the point of being impossible. So which things should we choose to believe in?
            <br>
            <br>
            Long argument:
            <br>
            When I talk to atheists, I try to bring up this argument to see how much thought they've given the idea of god's existence and how emotionally based their stance is. God could exist outside of this universe, so we can't rationally say "no god exists." The argument really is: if you cannot prove god does not exist, there remains a possibility that there is a god.
            <br><br>
            Let's take this argument and change it a bit. Instead of talking about god, let's talk about some object like a book. Imagine if I said, "there's a book in space floating between the Earth and the Sun." To prove that there isn't a book in space, we would have to scan all the space between the Earth and Sun. Not only that, but we would have to be sure of our methods for searching to remove all doubt.
            <br><br>
            We can't prove the book does not exist, so should we believe that there is one? We could actually list an infinite number of things, a frozen cow, a bicycle, etc. and say they could exist in space. This doesn't prove they exist. We can also say that disproving something exists in this situation is really hard or impossible for us right now.
            <br><br>
            The easiest way to prove the claim is to show it exists. If a scan picks up the book in space, then we have evidence to believe the claim. This is why the "burden of proof" is often on the person making the "positive" claim (that something exists), especially when that claim appears unfalsifiable (god exists outside the universe).
            <br><br>
            So saying that there's some possibility that god exists doesn't really get us anywhere. What we have to discuss now is "why should we believe in god?" Since god could exist outside the universe, why can't there be several gods or beings? Actually, this doesn't give us evidence for most religious gods in particular; they could all equally exist given this argument.
            <br><br>
            1) This argument is quite old and my example is based on <a href="https://en.wikipedia.org/wiki/Russell%27s_teapot">Bertrand Russell's analogy to a teapot</a>.
            <br>
            <br>
          </td>
        </tr>
        <tr>
          <td>
            Key terms: <br>
            Lorem
            <br>
            <br>
            Short argument:
            <br>

            <br>
            <br>
            Long argument:
            <br>

            <br>
            <br>
          </td>
        </tr>

      </table>
    </div>

    <div id="footerContent"></div>

    <script>
    function argFunction() {
      // Declare variables
      var input, filter, table, tr, tdKey, tdShort, tdArg, i;
      input = document.getElementById("myInput");
      filter = input.value.toUpperCase();
      table = document.getElementById("argTable");
      tr = table.getElementsByTagName("tr");

      // Loop through all table rows, and hide those who don't match the search query
      for (i = 0; i < tr.length; i++) {
        tdArg = tr[i].getElementsByTagName("td")[2];
        if (tdArg) {
          tdKey = tr[i].getElementsByTagName("td")[0];
          tdShort = tr[i].getElementsByTagName("td")[1];
          if ((tdArg.innerHTML.toUpperCase().indexOf(filter) > -1) || (tdKey.innerHTML.toUpperCase().indexOf(filter) > -1) || (tdShort.innerHTML.toUpperCase().indexOf(filter) > -1)) {
            tr[i].style.display = "";
          } else {
            tr[i].style.display = "none";
          }
        }
      }
    }
    </script>

  </body>
</html>


Good day, sir...I said good day!
