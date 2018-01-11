import { h, Component } from 'preact';
import 'preact-material-components/Button/style.css';
import Table from 'preact-material-components/Table';
import 'preact-material-components/Table/style.css';
import style from './style';

export default class Home extends Component {
	state = {
		builds = []
	}

	componentDidMount() {
		fetch('./api/v1/builds').then(
			results => { results.json() }
		).then(
			
		)
	}

	render() {
		return (
			<div class={style.home}>
				<h1>Home route</h1>
				<Table>
					<TableHeader>
						<TableRow>
							<TableHeaderColumn>Status</TableHeaderColumn>
							<TableHeaderColumn>Build #</TableHeaderColumn>
							<TableHeaderColumn>DateTime</TableHeaderColumn>
							<TableHeaderColumn></TableHeaderColumn>
						</TableRow>
						<TableBody>
							{ builds.map( build => (
								<TableRow>
									<TableRowColumn>{ build.status }</TableRowColumn>
									<TableRowColumn>{ build.id }</TableRowColumn>
									<TableRowColumn>{ build.timestamp }</TableRowColumn>
									<TableRowColumn>TODO: Actions?</TableRowColumn>
								</TableRow>
							)) }
						</TableBody>
					</TableHeader>
				</Table>
			</div>
		);
	}
}
