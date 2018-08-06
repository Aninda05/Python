def fitness(original, new):
    fitness = 0

    for x in range(0, width):
        for y in range(0, height):
            r1, g1, b1 = original.getpixel((x, y))
            r2, g2, b2 = new.getpixel((x, y))

            deltaRed = abs(r1 - r2)
            deltaGreen = abs(g1 - g2)
            deltaBlue = abs(b1 - b2)

            pixelFitness = pixelFitness = math.sqrt(deltaRed ** 2 + deltaGreen ** 2 + deltaBlue ** 2)

            fitness += pixelFitness

    return fitness