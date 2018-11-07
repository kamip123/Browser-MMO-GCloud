//alert("zaladowalo");
var game = new Phaser.Game(950, 650, Phaser.CANVAS, 'cityRenderDiv', { preload: preload, create: create, update: update, render: render });


function preload() {
    game.load.image('background', background); // ready
	game.load.image('barracks_1', barracks_1); // ready
	game.load.image('barracks_2', barracks_2); // ready
	game.load.image('energy_1',energy_1 ); // ready
	game.load.image('energy_2', energy_2); // ready
	game.load.image('farms_1', farms_1); // ready
	game.load.image('farms_2', farms_2); // ready
	game.load.image('housing_1', housing_1); // ready
	game.load.image('housing_2', housing_2); // ready
	game.load.image('mine_1', mine_1); // ready
	game.load.image('mine_2', mine_2); // ready
	game.load.image('roads_1', roads_1); // ready
	game.load.image('roads_2', roads_2); // ready
	game.load.image('town_hall_1', town_hall_1); // ready
	game.load.image('town_hall_2', town_hall_2); // ready
	game.load.image('town_hall_3', town_hall_3); // ready
}

var cursors;

var cityListInfo = [];
var infoPanel;
var text;



class townHall{
	constructor(lvl) {
		this.name = "Ratusz";
		this.lvl = lvl;
		if(lvl > 100){
			this.buildingIcon = "town_hall_3";
			this.sprite = game.add.sprite(530, 230, this.buildingIcon);
		}
		if(lvl>39 && lvl < 100){
			this.buildingIcon = "town_hall_2";
			this.sprite = game.add.sprite(530, 130, this.buildingIcon);
		}
		if(lvl < 40){
			this.buildingIcon = "town_hall_1";
			this.sprite = game.add.sprite(530, 230, this.buildingIcon);
		}
	}
}

class barracks{
	constructor(lvl) {
		this.name = "Barracks";
		this.lvl = lvl;
		if(lvl > 39){
			this.buildingIcon = "barracks_2";
			this.sprite = game.add.sprite(230, 270, this.buildingIcon);
		}
		if(lvl < 40){
			this.buildingIcon = "barracks_1";
			this.sprite = game.add.sprite(230, 270, this.buildingIcon);
		}
	}
}

class powerPlant{
	constructor(lvl) {
		this.name = "Power plant";
		this.lvl = lvl;
		if(lvl > 39){
			this.buildingIcon = "energy_2";
			this.sprite = game.add.sprite(880, 250, this.buildingIcon);
		}
		if(lvl < 40){
			this.buildingIcon = "energy_1";
			this.sprite = game.add.sprite(880, 250, this.buildingIcon);
		}
	}
}

class farms{
	constructor(lvl) {
		this.name = "Farms";
		this.lvl = lvl;
		if(lvl > 39){
			this.buildingIcon = "farms_2";
			this.sprite = game.add.sprite(0, 180, this.buildingIcon);
		}
		if(lvl < 40){
			this.buildingIcon = "farms_1";
			this.sprite = game.add.sprite(0, 180, this.buildingIcon);
		}
	}
}

class housing{
	constructor(lvl) {
		this.name = "Housing";
		this.lvl = lvl;
		if(lvl > 39){
			this.buildingIcon = "housing_2";
			this.sprite = game.add.sprite(20, 460, this.buildingIcon);
		}
		if(lvl < 40){
			this.buildingIcon = "housing_1";
			this.sprite = game.add.sprite(20, 460, this.buildingIcon);
		}
	}
}

class mine{
	constructor(lvl) {
		this.name = "Mine";
		this.lvl = lvl;
		if(lvl > 39){
			this.buildingIcon = "mine_2";
			this.sprite = game.add.sprite(900, 360, this.buildingIcon);
		}
		if(lvl < 40){
			this.buildingIcon = "mine_1";
			this.sprite = game.add.sprite(900, 360, this.buildingIcon);
		}
	}
}

class roads{
	constructor(lvl) {
		this.name = "Mine";
		this.lvl = lvl;
		if(lvl > 39){
			this.buildingIcon = "roads_2";
			this.sprite = game.add.sprite(0, 170, this.buildingIcon);
		}
		if(lvl < 40){
			this.buildingIcon = "roads_1";
			this.sprite = game.add.sprite(0, 170, this.buildingIcon);
		}
	}
}


function create() {

	game.world.setBounds(-0, -0, 1155, 800);

	
	//text = game.add.text(1, 1, '', { font:"10px Arial", fill: 'black' });
	
	game.add.sprite(0, 0, 'background');
	farms = new farms(poziomfarms);
	roads = new roads(poziomroads);
	townHall = new townHall(poziomtownHall);
	barracks = new barracks(poziombarracks);
	powerPlant = new powerPlant(poziompowerPlant);
	housing = new housing(50);
	//housing = new housing(poziomhousing);
	mine = new mine(poziommine);
	
	//text.text = townHallVariable.name + "\n" + townHallVariable.lvl;
	
	
    cursors = game.input.keyboard.createCursorKeys();
    game.world.scale.set(0.82)
}

function listenerClickBuilding() {
	
}

function update() {

    if (cursors.up.isDown)
    {
        game.camera.y -= 4;
    }
    else if (cursors.down.isDown)
    {
        game.camera.y += 4;
    }

    if (cursors.left.isDown)
    {
        game.camera.x -= 4;
    }
    else if (cursors.right.isDown)
    {
        game.camera.x += 4;
    }

}

function render() {

}
