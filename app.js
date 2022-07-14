let botao_descer = document.querySelector('.botao_baixo');
let botao = document.querySelector('button')

botao_descer.onclick = function () {
    scrollTo(0, 1000)
}

intro = d3.select('.intro')
svg = intro.append('svg').attr('height', '90vh').attr('width', '90vw')

rect1 = svg.append('rect')
    .attr('class', 'quadrado1')
    .attr('fill', '#C7D4F0')
    .attr('width', '20vh')
    .attr('height', '20vh')
    .attr('x', '10vw')
    .attr('y', 400)

rect2 = svg.append('rect')
    .attr('class', 'quadrado1')
    .attr('fill', '#C7D4F0')
    .attr('width', '20vh')
    .attr('height', '20vh')
    .attr('x', '10vw')
    .attr('y', 150)

rect3 = svg.append('rect')
    .attr('class', 'quadrado2')
    .attr('fill', '#C7D4F0')
    .attr('width', '20vh')
    .attr('height', '20vh')
    .attr('x', '10vw')
    .attr('y', 150)

rect4 = svg.append('rect')
    .attr('class', 'quadrado2')
    .attr('fill', '#C7D4F0')
    .attr('width', '20vh')
    .attr('height', '20vh')
    .attr('x', '10vw')
    .attr('y', 400)

rect5 = svg.append('rect')
    .attr('class', 'quadrado3')
    .attr('fill', '#C7D4F0')
    .attr('width', '20vh')
    .attr('height', '20vh')
    .attr('x', '10vw')
    .attr('y', 150)
    
rect6 = svg.append('rect')
    .attr('class', 'quadrado3')
    .attr('fill', '#C7D4F0')
    .attr('width', '20vh')
    .attr('height', '20vh')
    .attr('x', '10vw')
    .attr('y', 400)

rect = svg.append('rect')
    .attr('id', 'rect')
    .attr('width', '30vw')
    .attr('height', '60vh')
    .attr('x', 40)
    .attr('y', 120)
    .style('fill', '#677AA3')
    .attr('stroke', 'black')

text = svg.append('text').text('Dados inteligentes')
    .attr('id', 'texto1')
    .attr('x', '10vw')
    .attr('y', '50vh')
    .attr('fill', 'white')
    .attr('font-size', '3rem')
    .attr("transform", "rotate(-40)")

dinamico = svg.append('text').text('e dinâmicos')
    .attr('id', 'texto2')
    .attr('x', '5vw')
    .attr('y', '55vh')
    .attr('fill', '#677AA3')
    .attr('font-size', '3rem')




function triggerTransitionPiping() {
    d3.select("#texto1")
        .transition()
        .duration(2000)
        .attr("transform", "rotate(0)")
        .attr('x', '5vw')
        .attr('y', '45vh')
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
        .attr('x', '40vw')

    d3.selectAll('.quadrado2')
        .transition()
        .delay(4000)
        .duration(2000)
        .attr('x', '60vw')
    
    d3.selectAll('.quadrado3')
        .transition()
        .delay(4000)
        .duration(2000)
        .attr('x', '80vw')

}

botao.onclick = triggerTransitionPiping