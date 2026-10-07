<!DOCTYPE html>
<html>
<head>
<style>
.heart {
  width: 100px;
  height: 90px;
  position: relative;
  margin: 100px auto;
  background: red;
  transform: rotate(-45deg);
  animation: beat 1s infinite;
}
.heart:before, .heart:after {
  content: "";
  width: 100px;
  height: 90px;
  background: red;
  border-radius: 50%;
  position: absolute;
}
.heart:before { top: -45px; left: 0; }
.heart:after { left: 45px; top: 0; }

@keyframes beat {
  0% { transform: rotate(-45deg) scale(1); }
  50% { transform: rotate(-45deg) scale(1.1); }
}
</style>
</head>
<body>
<div class="heart"></div>
</body>
</html>
