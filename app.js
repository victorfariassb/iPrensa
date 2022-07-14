let botao_descer = document.querySelector('.botao_baixo');
let botao = document.querySelector('button')

botao_descer.onclick = function () {
    scrollTo(0, 715)
}

intro = d3.select('.intro')
svg = intro.append('svg').attr('height', 710).attr('width', 1350)

rect1 = svg.append('rect')
    .attr('class', 'quadrado1')
    .attr('fill', '#C7D4F0')
    .attr('width', '200')
    .attr('height', '200')
    .attr('x', 40)
    .attr('y', 400)

rect2 = svg.append('rect')
    .attr('class', 'quadrado1')
    .attr('fill', '#C7D4F0')
    .attr('width', '200')
    .attr('height', '200')
    .attr('x', 40)
    .attr('y', 150)

rect3 = svg.append('rect')
    .attr('class', 'quadrado2')
    .attr('fill', '#C7D4F0')
    .attr('width', '200')
    .attr('height', '200')
    .attr('x', 275)
    .attr('y', 150)

rect4 = svg.append('rect')
    .attr('class', 'quadrado2')
    .attr('fill', '#C7D4F0')
    .attr('width', '200')
    .attr('height', '200')
    .attr('x', 275)
    .attr('y', 400)

rect = svg.append('rect')
    .attr('id', 'rect')
    .attr('width', 500)
    .attr('height', 500)
    .attr('x', 40)
    .attr('y', 120)
    .style('fill', '#677AA3')
    .attr('stroke', 'black')
text = svg.append('text').text('Dados inteligentes')
    .attr('id', 'texto1')
    .attr('x', 250)
    .attr('y', 100)
    .attr('fill', 'white')
    .attr('font-size', '3rem')
    .attr("transform", "rotate(-40)")

dinamico = svg.append('text').text('e dinâmicos')
    .attr('id', 'texto2')
    .attr('x', 100)
    .attr('y', 400)
    .attr('fill', '#677AA3')
    .attr('font-size', '3rem')




function triggerTransitionPiping () {
    d3.select("#texto1")
    .transition()
    .duration(2000)
    .attr("transform", "rotate(0)")
    .attr('x', 100)
    .attr('y', 350)
    .end()

    d3.select("#texto2")
    .transition()
    .style("fill", "white")
    .delay(2000)
    .duration(2000)

    d3.selectAll('.quadrado1')
    .transition()
    .delay(4000)
    .duration(2000)
    .attr('x', 1000)

    d3.selectAll('.quadrado2')
    .transition()
    .delay(4000)
    .duration(2000)
    .attr('x', 700)

}

botao.onclick = triggerTransitionPiping