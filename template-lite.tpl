<html>

<head>
    <title>@{{username}}</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://code.jquery.com/jquery-3.1.0.min.js" integrity="sha256-cCueBR6CsyA4/9szpPfrX3s49M9vUU5BgtiJj06wt/s=" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</head>

<body style="background-color:#444">
    <div class="container" style="margin-top:2em;">

        <nav class="navbar navbar-inverse">
            <div class="container">
                <div class="navbar-header">
                    <a class="navbar-brand" href="#">{{username}}</a>
                </div>
            </div>
        </nav>
           <div class="col-sm-6">
                <div class="panel panel-primary">
                    <div class="panel-heading">
                        <h3>Not Followed Back</h3>
                    </div>
                    <div class="panel-body">
                        <table class="table table-hover">
                            <thead>
                                <tr>
                                    <th>Full Name</th>
                                    <th>User Name</th>
                                    <th>Image</th>
                                </tr>
                            </thead>
                            <tbody>
                                {{#notback}}
                                <tr>
                                    <td>{{full_name}}</td>
                                    <td>{{username}}</td>
                                    <td><img src="{{profile_pic_url}}" class="img img-responsive center-block img-circle" style="width:50px; height:50px;" /></td>
                                </tr>
                                {{/notback}}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>

        <div class="row">
            <div class="col-sm-6">
                <div class="panel panel-warning">
                    <div class="panel-heading">
                        <h3>New Followers :)</h3>
                    </div>
                    <div class="panel-body">
                        <table class="table table-hover">
                            <thead>
                                <tr>
                                    <th>Full Name</th>
                                    <th>User Name</th>
                                    <th>Image</th>
                                </tr>
                            </thead>
                            <tbody>
                                {{#newfollowers}}
                                <tr>
                                    <td>{{full_name}}</td>
                                    <td>{{username}}</td>
                                    <td><img src="{{profile_pic_url}}" class="img img-responsive center-block img-circle" style="width:50px; height:50px;" /></td>
                                </tr>
                                {{/newfollowers}}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

        <div class="row">
            <div class="col-sm-6">
                <div class="panel panel-warning">
                    <div class="panel-heading">
                        <h3>New Unfollowers :(</h3>
                    </div>
                    <div class="panel-body">
                        <table class="table table-hover">
                            <thead>
                                <tr>
                                    <th>Full Name</th>
                                    <th>User Name</th>
                                    <th>Image</th>
                                </tr>
                            </thead>
                            <tbody>
                                {{#newunfollowers}}
                                <tr>
                                    <td>{{full_name}}</td>
                                    <td>{{username}}</td>
                                    <td><img src="{{profile_pic_url}}" class="img img-responsive center-block img-circle" style="width:50px; height:50px;" /></td>
                                </tr>
                                {{/newunfollowers}}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
 
            <div class="col-sm-6">
                <div class="panel panel-warning">
                    <div class="panel-heading">
                        <h3>New Followings</h3>
                    </div>
                    <div class="panel-body">
                        <table class="table table-hover">
                            <thead>
                                <tr>
                                    <th>Full Name</th>
                                    <th>User Name</th>
                                    <th>Image</th>
                                </tr>
                            </thead>
                            <tbody>
                                {{#newfollowings}}
                                <tr>
                                    <td>{{full_name}}</td>
                                    <td>{{username}}</td>
                                    <td><img src="{{profile_pic_url}}" class="img img-responsive center-block img-circle" style="width:50px; height:50px;" /></td>
                                </tr>
                                {{/newfollowings}}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>


        <nav class="navbar navbar-inverse navbar-static-bottom">
            <div class="container">
                <h4 class="text-center" style="color:white; margin-top:15px;">btyb Cagri Ozkan</h4>         
            </div>
        </nav>
    </div>
</body>

</html>
