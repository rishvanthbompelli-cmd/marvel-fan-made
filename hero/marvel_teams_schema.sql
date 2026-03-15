-- ============================================================
-- MARVEL UNIVERSE DATABASE SCHEMA
-- Scalable structure for 200+ characters
-- ============================================================

-- ============================================================
-- TABLE: teams
-- Stores all Marvel teams/groups
-- ============================================================
CREATE TABLE IF NOT EXISTS teams (
    id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    color VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================================
-- TABLE: heroes
-- Main characters table with team associations
-- ============================================================
CREATE TABLE IF NOT EXISTS heroes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    team_id VARCHAR(50) NOT NULL,
    role ENUM('Hero', 'Villain', 'Anti-Hero', 'Cosmic Entity') NOT NULL DEFAULT 'Hero',
    description TEXT,
    image VARCHAR(255),
    category VARCHAR(50) DEFAULT 'marvel',
    power_level INT DEFAULT 50,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (team_id) REFERENCES teams(id) ON DELETE CASCADE,
    INDEX idx_team (team_id),
    INDEX idx_role (role),
    INDEX idx_category (category),
    INDEX idx_name (name)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================================
-- TABLE: hero_stats
-- Scalable stats for each hero (can add more stats easily)
-- ============================================================
CREATE TABLE IF NOT EXISTS hero_stats (
    id INT AUTO_INCREMENT PRIMARY KEY,
    hero_id INT NOT NULL,
    stat_name VARCHAR(50) NOT NULL,
    stat_value INT DEFAULT 0,
    FOREIGN KEY (hero_id) REFERENCES heroes(id) ON DELETE CASCADE,
    UNIQUE KEY unique_hero_stat (hero_id, stat_name),
    INDEX idx_hero (hero_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================================
-- TABLE: team_filters
-- Dynamic filter tabs for UI
-- ============================================================
CREATE TABLE IF NOT EXISTS team_filters (
    id INT AUTO_INCREMENT PRIMARY KEY,
    team_id VARCHAR(50) NOT NULL,
    filter_name VARCHAR(100),
    filter_value VARCHAR(100),
    sort_order INT DEFAULT 0,
    FOREIGN KEY (team_id) REFERENCES teams(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- ============================================================
-- INSERT TEAMS DATA
-- ============================================================
INSERT INTO teams (id, name, description, color) VALUES
('avengers', 'Avengers', 'Earth''s mightiest heroes protecting the planet from threats', '#e62429'),
('xmen', 'X-Men', 'Mutant heroes fighting for peace between mutants and humans', '#1e90ff'),
('guardians', 'Guardians of the Galaxy', 'Cosmic outlaws protecting the galaxy', '#9b59b6'),
('cosmic', 'Cosmic Entities', 'Universal beings of immense power', '#f39c12'),
('spiderverse', 'Spider-Verse', 'Web-slingers from across dimensions', '#e74c3c'),
('mystic', 'Mystic / Magic', 'Masters of the mystical arts', '#8e44ad'),
('street', 'Street Level', 'Heroes from the mean streets', '#27ae60');

-- ============================================================
-- INSERT HEROES DATA (Avengers)
-- ============================================================
INSERT INTO heroes (name, team_id, role, description, image, category) VALUES
('Iron Man', 'avengers', 'Hero', 'Genius billionaire Tony Stark fights crime in his powered suit of armor.', 'Iron-Man.jpg', 'marvel'),
('Captain America', 'avengers', 'Hero', 'Steve Rogers, the super-soldier, leads the Avengers with honor.', 'captain america.jpg', 'marvel'),
('Thor', 'avengers', 'Hero', 'The God of Thunder, protector of Earth and Asgard.', 'thor.jpg', 'marvel'),
('Hulk', 'avengers', 'Hero', 'Bruce Banner transforms into the powerful Hulk when angry.', 'hulk.jpg', 'marvel'),
('Black Widow', 'avengers', 'Hero', 'Natasha Romanoff, the world''s greatest spy and assassin.', 'black widow.jpg', 'marvel'),
('Hawkeye', 'avengers', 'Hero', 'Clint Barton, the world''s greatest marksman.', 'hawkeye.jpg', 'marvel'),
('Scarlet Witch', 'avengers', 'Hero', 'Wanda Maximoff, mutant with reality-warping powers.', 'scarlet witch.jpg', 'marvel'),
('Vision', 'avengers', 'Hero', 'An android created by Ultron, possesses the Mind Stone.', 'vision.jpg', 'marvel'),
('Falcon', 'avengers', 'Hero', 'Sam Wilson, ex-paratrooper with a winged suit.', 'falcon.jpg', 'marvel'),
('War Machine', 'avengers', 'Hero', 'James Rhodes, pilot of the War Machine armor.', 'war machine.jpg', 'marvel'),
('Ant-Man', 'avengers', 'Hero', 'Scott Lang, hero who can shrink and control insects.', 'ant-man.jpg', 'marvel'),
('Wasp', 'avengers', 'Hero', 'Hope van Dyne, daughter of Hank Pym with similar Pym Particles abilities.', 'wasp.jpg', 'marvel'),
('Black Panther', 'avengers', 'Hero', 'T''Challa, King of Wakanda with Vibranium suit.', 'black panther.jpg', 'marvel'),
('Captain Marvel', 'avengers', 'Hero', 'Carol Danvers, half-Kree warrior with cosmic powers.', 'captain marvel.jpg', 'marvel'),
('Spider-Man', 'avengers', 'Hero', 'Peter Parker, the friendly neighborhood Spider-Man.', 'spider-man.jpg', 'marvel'),
('She-Hulk', 'avengers', 'Hero', 'Jennifer Walters, lawyer and green powerhouse.', 'she-hulk.jpg', 'marvel'),
('Shang-Chi', 'avengers', 'Hero', 'Master of Kung Fu, trained in the Ten Rings.', 'shang-chi.jpg', 'marvel'),
('Moon Knight', 'avengers', 'Hero', 'Marc Spector, avatar of the Egyptian moon god Khonshu.', 'moon knight.jpg', 'marvel'),
('Ultron', 'avengers', 'Villain', 'AI villain created by Hank Pym, obsessed with extinction.', 'ultron.jpg', 'marvel'),
('Deadpool', 'avengers', 'Anti-Hero', 'Wade Wilson, mercenary with regenerative healing.', 'deapool.jpg', 'marvel');

-- ============================================================
-- INSERT HEROES DATA (X-Men)
-- ============================================================
INSERT INTO heroes (name, team_id, role, description, image, category) VALUES
('Professor X', 'xmen', 'Hero', 'Charles Xavier, founder of Xavier''s School for Gifted Youngsters.', 'professor x.jpg', 'marvel'),
('Wolverine', 'xmen', 'Hero', 'Logan, mutant with regenerative healing and claws.', 'wolverine.jpg', 'marvel'),
('Cyclops', 'xmen', 'Hero', 'Scott Summers, leader of the X-Men with optic blasts.', 'cyclops.jpg', 'marvel'),
('Jean Grey', 'xmen', 'Hero', 'Powerful telepath and telekinetic, host to Phoenix Force.', 'jean grey.jpg', 'marvel'),
('Storm', 'xmen', 'Hero', 'Ororo Munroe, weather manipulator and Queen of Wakanda.', 'storm.jpg', 'marvel'),
('Beast', 'xmen', 'Hero', 'Hank McCoy, mutated genius with superhuman abilities.', 'beast.jpg', 'marvel'),
('Rogue', 'xmen', 'Hero', 'Anna Marie, absorbs powers and memories through touch.', 'rogue.jpg', 'marvel'),
('Gambit', 'xmen', 'Hero', 'Remy LeBeau, expert thief with kinetic charging abilities.', 'gambit.jpg', 'marvel'),
('Nightcrawler', 'xmen', 'Hero', 'Kurt Wagner, teleporting mutant with demonic appearance.', 'nightcrawler.jpg', 'marvel'),
('Iceman', 'xmen', 'Hero', 'Bobby Drake, mutant who can generate and control ice.', 'iceman.jpg', 'marvel'),
('Colossus', 'xmen', 'Hero', 'Peter Rasputin, can transform his body into organic steel.', 'colossus.jpg', 'marvel'),
('Kitty Pryde', 'xmen', 'Hero', 'Kate Pryde, phasing mutant and team leader.', 'kitty pryde.jpg', 'marvel'),
('Psylocke', 'xmen', 'Hero', 'Betsy Braddock, telepath and martial artist.', 'psylocke.jpg', 'marvel'),
('Magneto', 'xmen', 'Villain', 'Erik Lehnsherr, master of magnetism and mutant supremacist.', 'magneto.jpg', 'marvel'),
('Mystique', 'xmen', 'Villain', 'Raven Darkhölme, shapeshifter and mutant activist.', 'mystique.jpg', 'marvel'),
('Sabretooth', 'xmen', 'Villain', 'Victor Creed, feral mutant with enhanced senses.', 'sabretooth.jpg', 'marvel'),
('Apocalypse', 'xmen', 'Villain', 'En Sabah Nur, ancient mutant seeking world domination.', 'apocalypse.jpg', 'marvel'),
('Mr. Sinister', 'xmen', 'Villain', 'Nathaniel Essex, twisted geneticist experimenting on mutants.', 'mr sinister.jpg', 'marvel');

-- ============================================================
-- INSERT HEROES DATA (Guardians of the Galaxy)
-- ============================================================
INSERT INTO heroes (name, team_id, role, description, image, category) VALUES
('Star-Lord', 'guardians', 'Hero', 'Peter Quill, half-human leader of the Guardians.', 'star-lord.jpg', 'marvel'),
('Gamora', 'guardians', 'Hero', 'Deadliest woman in the galaxy, adopted daughter of Thanos.', 'gamora.jpg', 'marvel'),
('Drax', 'guardians', 'Hero', 'Arthur Douglas, powerful warrior seeking vengeance on Thanos.', 'drax.jpg', 'marvel'),
('Rocket Raccoon', 'guardians', 'Hero', 'Genetically modified raccoon, master of weapons.', 'rocket.jpg', 'marvel'),
('Groot', 'guardians', 'Hero', 'Flora Colossus, talking tree with regenerative abilities.', 'groot.jpg', 'marvel'),
('Mantis', 'guardians', 'Hero', 'Empathic alien with emotional manipulation powers.', 'mantis.jpg', 'marvel'),
('Nebula', 'guardians', 'Anti-Hero', 'Cybernetically enhanced alien, sister to Gamora.', 'nebula.jpg', 'marvel'),
('Adam Warlock', 'guardians', 'Hero', 'Synthetic being with cosmic powers, guardian of the Soul Gem.', 'adam warlock.jpg', 'marvel'),
('Nova', 'guardians', 'Hero', 'Richard Rider, last surviving Nova Centurion.', 'nova.jpg', 'marvel');

-- ============================================================
-- INSERT HEROES DATA (Cosmic Entities)
-- ============================================================
INSERT INTO heroes (name, team_id, role, description, image, category) VALUES
('Thanos', 'cosmic', 'Villain', 'The Mad Titan, collector of Infinity Stones.', 'thanos.jpg', 'marvel'),
('Silver Surfer', 'cosmic', 'Hero', 'Norrin Radd, herald of Galactus with cosmic powers.', 'silver surfer.jpg', 'marvel'),
('Galactus', 'cosmic', 'Cosmic Entity', 'The World-Eater, cosmic giant that consumes planets.', 'galactus.jpg', 'marvel'),
('The Watcher', 'cosmic', 'Cosmic Entity', 'Uatu, cosmic observer sworn to never interfere.', 'watcher.jpg', 'marvel'),
('Eternity', 'cosmic', 'Cosmic Entity', 'Embodiment of time and all existence.', 'eternity.jpg', 'marvel'),
('Living Tribunal', 'cosmic', 'Cosmic Entity', 'Multiversal guardian of cosmic justice.', 'living tribunal.jpg', 'marvel'),
('Celestials', 'cosmic', 'Cosmic Entity', 'Elder gods who shaped the universe and mutate species.', 'celestials.jpg', 'marvel'),
('Kang the Conqueror', 'cosmic', 'Villain', 'Nathaniel Richards, conqueror from the future.', 'kang.jpg', 'marvel');

-- ============================================================
-- INSERT HEROES DATA (Spider-Verse)
-- ============================================================
INSERT INTO heroes (name, team_id, role, description, image, category) VALUES
('Miles Morales', 'spiderverse', 'Hero', 'Young Spider-Man from Earth-1610 with venom powers.', 'miles morales.jpg', 'marvel'),
('Spider-Gwen', 'spiderverse', 'Hero', 'Gwen Stacy as Spider-Woman from Earth-65.', 'spider-gwen.jpg', 'marvel'),
('Venom', 'spiderverse', 'Anti-Hero', 'Eddie Brock, bonded with alien symbiote.', 'venom.jpg', 'marvel'),
('Carnage', 'spiderverse', 'Villain', 'Cletus Kasady, bonded with red symbiote.', 'carnage.jpg', 'marvel'),
('Green Goblin', 'spiderverse', 'Villain', 'Norman Osborn, Spider-Man''s greatest enemy.', 'green goblin.jpg', 'marvel'),
('Doctor Octopus', 'spiderverse', 'Villain', 'Otto Octavius, genius with mechanical tentacles.', 'doctor octopus.jpg', 'marvel'),
('Sandman', 'spiderverse', 'Anti-Hero', 'Flint Marko, morphs into sand.', 'sandman.jpg', 'marvel'),
('Lizard', 'spiderverse', 'Villain', 'Curt Connors, transformed into giant reptile.', 'lizard.jpg', 'marvel');

-- ============================================================
-- INSERT HEROES DATA (Mystic / Magic)
-- ============================================================
INSERT INTO heroes (name, team_id, role, description, image, category) VALUES
('Doctor Strange', 'mystic', 'Hero', 'Stephen Strange, Sorcerer Supreme and master of mystic arts.', 'doctor strange.jpg', 'marvel'),
('Loki', 'mystic', 'Anti-Hero', 'God of Mischief, master of illusion and sorcery.', 'loki.jpg', 'marvel'),
('Wong', 'mystic', 'Hero', 'Master of the mystic arts, protector of Sanctums.', 'wong.jpg', 'marvel'),
('Agatha Harkness', 'mystic', 'Anti-Hero', 'Ancient witch, former mentor to Scarlet Witch.', 'agatha harkness.jpg', 'marvel'),
('Ghost Rider', 'mystic', 'Hero', 'Johnny Blaze, demonic spirit of vengeance.', 'ghost rider.jpg', 'marvel'),
('Blade', 'mystic', 'Hero', 'Daywalker, half-vampire vampire hunter.', 'blade.jpg', 'marvel');

-- ============================================================
-- INSERT HEROES DATA (Street Level)
-- ============================================================
INSERT INTO heroes (name, team_id, role, description, image, category) VALUES
('Daredevil', 'street', 'Hero', 'Matt Murdock, blind lawyer with heightened senses.', 'daredevil.jpg', 'marvel'),
('Luke Cage', 'street', 'Hero', 'Hero for Hire, unbreakable powerhouse.', 'luke cage.jpg', 'marvel'),
('Iron Fist', 'street', 'Hero', 'Danny Rand, martial artist with iron fist power.', 'iron fist.jpg', 'marvel'),
('Jessica Jones', 'street', 'Hero', 'Private investigator with superhuman strength.', 'jessica jones.jpg', 'marvel'),
('Punisher', 'street', 'Anti-Hero', 'Frank Castle, vigilante lethal against criminals.', 'punisher.jpg', 'marvel'),
('Echo', 'street', 'Hero', 'Maya Lopez, deaf mutant with photographic reflexes.', 'echo.jpg', 'marvel');

-- ============================================================
-- SAMPLE HERO STATS (Scalable)
-- ============================================================
INSERT INTO hero_stats (hero_id, stat_name, stat_value) VALUES
(1, 'intelligence', 95),
(1, 'strength', 85),
(1, 'speed', 70),
(1, 'durability', 80),
(2, 'intelligence', 80),
(2, 'strength', 90),
(2, 'speed', 60),
(2, 'durability', 95),
(3, 'intelligence', 75),
(3, 'strength', 100),
(3, 'speed', 80),
(3, 'durability', 100);

-- ============================================================
-- TEAM FILTERS FOR UI (Dynamic)
-- ============================================================
INSERT INTO team_filters (team_id, filter_name, filter_value, sort_order) VALUES
('avengers', 'All', 'all', 1),
('avengers', 'Heroes', 'Hero', 2),
('avengers', 'Villains', 'Villain', 3),
('xmen', 'All', 'all', 1),
('xmen', 'Heroes', 'Hero', 2),
('xmen', 'Villains', 'Villain', 3),
('guardians', 'All', 'all', 1),
('spiderverse', 'All', 'all', 1),
('spiderverse', 'Heroes', 'Hero', 2),
('spiderverse', 'Villains', 'Villain', 3),
('mystic', 'All', 'all', 1),
('street', 'All', 'all', 1);
