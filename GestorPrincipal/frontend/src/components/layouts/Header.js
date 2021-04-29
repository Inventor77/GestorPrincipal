import React, { Component } from "react";

export class Header extends Component {
	render() {
		return (
			<div>
				<nav className="navbar navbar-expand-sm navbar-light bg-light">
					<div className="container-fluid">
						<a className="navbar-brand" href="#">
							GestorPrincipal
						</a>
					</div>
				</nav>
			</div>
		);
	}
}

export default Header;
