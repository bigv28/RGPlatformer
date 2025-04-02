def game_loop(delta_time):
    # Update player animation
    player.update_animation(delta_time)
    
    # Check collisions
    interaction.enemy_collision()
    