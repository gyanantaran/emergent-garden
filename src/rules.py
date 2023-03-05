
# RULES
apply_rule(self.dt, self.red_particles, self.red_particles, +0.1)
apply_rule(self.dt, self.yellow_particles, self.yellow_particles, +0.3)
apply_rule(self.dt, self.green_particles, self.green_particles, -0.1)
apply_rule(self.dt, self.blue_particles, self.blue_particles, -0.2)

apply_rule(self.dt, self.red_particles, self.yellow_particles, +0.5)
apply_rule(self.dt, self.red_particles, self.green_particles, -0.05)
apply_rule(self.dt, self.red_particles, self.blue_particles, +0.07)

apply_rule(self.dt, self.yellow_particles, self.green_particles, -0.3)
apply_rule(self.dt, self.yellow_particles, self.red_particles, +0.05)
apply_rule(self.dt, self.yellow_particles, self.blue_particles, +0.1)

apply_rule(self.dt, self.green_particles, self.green_particles, -0.1)
apply_rule(self.dt, self.green_particles, self.yellow_particles, 0.2)
apply_rule(self.dt, self.green_particles, self.blue_particles, 0.02)

apply_rule(self.dt, self.blue_particles, self.red_particles, +0.1)
apply_rule(self.dt, self.blue_particles, self.yellow_particles, -0.1)
apply_rule(self.dt, self.blue_particles, self.green_particles, -0.2)


# PARTICLE GROUPS
self.red_particles = instantiateGroup(num=PARTICLE_DEFAULT_SPAWN_NUM, c=PARTICLE_COLOR_RED, frame=PARTICLE_DEFAULT_SPAWN_FRAME)
self.yellow_particles = instantiateGroup(num=PARTICLE_DEFAULT_SPAWN_NUM, c=PARTICLE_COLOR_YELLOW, frame=PARTICLE_DEFAULT_SPAWN_FRAME)
self.green_particles = instantiateGroup(num=PARTICLE_DEFAULT_SPAWN_NUM, c=PARTICLE_COLOR_GREEN, frame=PARTICLE_DEFAULT_SPAWN_FRAME)
self.blue_particles = instantiateGroup(num=PARTICLE_DEFAULT_SPAWN_NUM, c=PARTICLE_COLOR_BLUE, frame=PARTICLE_DEFAULT_SPAWN_FRAME)



for particle in self.yellow_particles:
    particle.draw(self.screen)

for particle in self.green_particles:
    particle.draw(self.screen)

for particle in self.blue_particles:
    particle.draw(self.screen)
