from app import app
from models import db, ground_position, phase, move, standing


db.drop_all()
db.create_all()

g1 = ground_position(
    groundPositionCode = "Open_Guard",
    name="Open Guard",
    info="As the bottom athlete, your legs and hips are in front of your opponent, acting as shields to protect yourself from any submissions or strikes from your opponent. As the top athlete, your job is to control your opponent to pass his hips and legs.",
    image = "https://cdn.evolve-vacation.com/wp-content/uploads/2018/02/open-guard-bjj.jpg",
    imageCredit = "Evolve Vacation.com"
)

g2 = ground_position(
    groundPositionCode = "Half_Guard",
    name="Half Guard",
    info="Half guard is one of the best positions for the top athlete to pass your opponent's guard to either side control or top-mount. Surprisingly, half-guard is also the best position to maintain control and protect yourself from submissions and strikes from the top athlete.",
    image = "https://cdn.shopify.com/s/files/1/1800/2299/articles/tomhalf_9e3d20e1-f108-40ce-ad06-212c97eb653f_1024x1024.jpg?v=1509340082",
    imageCredit = "BJJ Fanatics"
)

g3 = ground_position(
    groundPositionCode = "Side_Control",
    name="Side Control",
    info= "Side control is when the top athlete is perpendicular to the bottom athlete and can control his or her opponent from the side of the body. This is an ideal position for controlling the bottom athlete and can lead to powerful submissions. As the bottom athlete, your guard has been passed and you need to either re-guard or use a move to sweep your opponent.",
    image = "https://www.bjjee.com/wp-content/uploads/2020/09/bjj-side-control-escape.jpg",
    imageCredit = "bjjee.com"
)

g4 = ground_position(
    groundPositionCode = "Closed_Guard",
    name="Closed Guard",
    info= "Closed guard is when the bottom athlete has both of their legs wrapped around their opponent. This is an effective defensive position that restricts your opponent's. The closed guard also allows the bottom athlete to either sweep or attack with submissions. As the top athlete, your ultimate job is to break your opponent's closed guard or wrapped legs around your waist.",
    image = "https://cdn.shopify.com/s/files/1/1800/2299/articles/Screenshot_2019-10-30_at_1.11.57_PM_1024x1024.png?v=1572455553",
    imageCredit = "BJJ Finatics"
)

g5 = ground_position(
    groundPositionCode = "Top_Mount",
    name="Top Mount",
    info= "For the top athlete, the top mount is a highly effective attacking position. There are various strikes and submissions which you can use to finish a fight. However, as the bottom athlete, you must work to get out of this position.",
    image = "https://www.bjjee.com/wp-content/uploads/2019/12/armbar-mount.jpg",
    imageCredit = "bjjee.com"
)

g6 = ground_position(
    groundPositionCode = "Back_Mount",
    name="Back Mount",
    info= "In the view of most Jiujitsu practitioners is the ultimate position to control your opponent and finish the fight with strikes and submissions. However,  the athlete with their back-mounted, you must protect your kneck and utilize technique to escape this position. ",
    image = "https://www.jiujitsutimes.com/wp-content/uploads/Screenshot-1347.png",
    imageCredit = "Jiujitsutimes.com"
)

p1 = phase(
    name="Standing Position",
    info= "All fights start on the feet where your opponent has their maximum striking potential. Minimize your opponent's explosiveness by taking your opponent to the ground.",
    image = "https://www.bjjee.com/wp-content/uploads/2020/09/collar-drag.jpg",
    imageCredit = "BJJ Finatics"
)

p2 = phase(
    name="Ground Position",
    info= "Taking your opponent to the ground allows you to use your body position and technique to control your opponent and ultimately end the fight through strikes or submissions.",
    image = "https://d2779tscntxxsw.cloudfront.net/5edb2956204af.png?width=1000",
    imageCredit = "flograppling.com"
)

m1 = move(
    name="Rear Naked Choke",
    info= "Choke Your Opponent From Behind.",
    image = "https://grapplinginsider.com/wp-content/uploads/2021/03/john-danaher-720x445.jpg",
    groundPositionCode = "Back_Mount",
    imageCredit = "grapplinginsider.com"
)

m2 = move(
    name="Arm Bar",
    info= "Break your opponent's arm from the top mount position",
    image = "https://cdn.shopify.com/s/files/1/1800/2299/articles/hi-res-8068de0b8115e6f0689d253794b11032_crop_north_1024x1024.jpg?v=1521495266",
    groundPositionCode = "Top_Mount",
    imageCredit = "BJJ Finatics"
)

m3 = move(
    name="Kimura",
    info= "Break your opponent's arm from the side mount position",
    image = "https://www.grapplearts.com/wp-content/uploads/2018/03/closed-guard-Kimura-armlock-from-closed-guard.png",
    groundPositionCode = "Side_Control",
    imageCredit = "grapplearts.com"
)

m4 = move(
    name="Triangle",
    info= "Use your legs the strongest part of your body, against your opponent's weaker upperbody. Wrap your legs around their neck and below their shoulder to compress the arteries around their kneck",
    image = "https://cdn.shopify.com/s/files/1/1800/2299/articles/trianglexxxx_1024x1024.jpg?v=1604447283",
    groundPositionCode = "Closed_Guard",
    imageCredit = "BJJ Finatics"
)

m5 = move(
    name="Old School Sweep",
    info= "From the half guard position ontain a deep underhook on your opponent, reach with the opposite hand and grab your opponent's foot. Pass foot to other handm and with that same hand grab their thigh from the outside. Push into them, and obtain the sweep.",
    image = "https://www.bjjee.com/wp-content/uploads/2020/12/old-school-sweep.jpg",
    groundPositionCode = "Half_Guard",
    imageCredit = "bjjee.com"
)

m6 = move(
    name="Guard Retention",
    info= "This is a defensive position, keep your legs and hips in front of your opponent. Doing so will keep you protected from their strikes. Do your best to establish connection with your 2 hands and feet to your opponent. This will help you control your opponent;s movements",
    image = "https://www.grapplearts.com/wp-content/uploads/2016/08/guard-retention.png",
    groundPositionCode = "Open_Guard",
    imageCredit = "grapplearts.com"
)

s1 = standing(
    name="Double Leg",
    info= "Wrap both arms around your opponent's legs and take him to the ground",
    image = "https://cdn.shopify.com/s/files/1/1800/2299/articles/153398ec3601a31fe8b61761d6a43f26_1024x1024.jpg?v=1549290519",
    imageCredit = "BJJ Finatics"
)



db.session.add_all([g1,g2,g3,g4,g5,g6,p1,p2,m1,m2,m3,m4,m5,m6,s1])
db.session.commit()






























